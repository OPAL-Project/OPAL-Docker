from __future__ import division, print_function
import time
import os
import configargparse
import bz2
import csv
import json
import sys
from datetime import datetime
from os import listdir
from os.path import isfile, join
import multiprocessing as mp


def process_file(records_reader, file):
    core_fields = {"file": file, "lines": 0, "calls": 0, "texts": 0, "NotWellFormedTooLong": 0,
                   "NotWellFormedTooShort": 0, "NotWellFormedWrongCallType": 0, "NotWellFormedWrongNumberFormat": 0,
                   "NotWellFormedDate": 0, "NotWellFormedCallDuration": 0}
    stats = dict(core_fields)
    stats["lines"] = 0
    for row in records_reader:
        # We compute the statistics for the row
        stats["lines"] = stats["lines"] + 1
        fields_vals = row[0].split(';')
        if len(fields_vals) < 9:
            stats["NotWellFormedTooShort"] = stats["NotWellFormedTooShort"] + 1
            continue
        if len(fields_vals) > 9:
            stats["NotWellFormedTooLong"] = stats["NotWellFormedTooLong"] + 1
            continue
        try:
            call_type = int(fields_vals[0])
            if not call_type in [1, 2]:
                stats["NotWellFormedWrongCallType"] = stats["NotWellFormedWrongCallType"] + 1
                continue
        except ValueError:
            stats["NotWellFormedWrongCallType"] = stats["NotWellFormedWrongCallType"] + 1
            continue
        try:
            int(fields_vals[1])
        except ValueError:
            stats["NotWellFormedWrongNumberFormat"] = stats["NotWellFormedWrongNumberFormat"] + 1
            continue
        try:
            int(fields_vals[6])
        except ValueError:
            stats["NotWellFormedWrongNumberFormat"] = stats["NotWellFormedWrongNumberFormat"] + 1
            continue
        try:
            datetime.strptime(fields_vals[2], '%Y-%m-%d %H:%M:%S')
        except ValueError:
            stats["NotWellFormedDate"] = stats["NotWellFormedDate"] + 1
            continue
        try:
            call_duration = int(fields_vals[8])
        except ValueError:
            stats["NotWellFormedCallDuration"] = stats["NotWellFormedCallDuration"] + 1
            continue
        if call_duration == 1 :
            stats["texts"] = stats["texts"] + 1
        else:
            stats["calls"] = stats["calls"] + 1
    return stats


# STATS to be extracted :
# 1) Total number of call and text per hour
# 2) Total number of unique numbers per hour
# 3) Check the pseudonymization (that the same number appear in all files)
# We process a file by first extracting the compressed data into a csv
def process_day(writing_queue, zip_files, path):
    for i in range(len(zip_files)):
        zip_file = zip_files[i]
        file_name = zip_file[:-4]  # assuming the filepath ends with .bz2
        zipfile = bz2.BZ2File(path + '/' + zip_file)  # open the file
        data = zipfile.read()  # get the decompressed data
        open(path + '/' + file_name, 'wb').write(data)  # write a uncompressed file
        csv_path = os.path.join(path, file_name)
        # csv_path = path + '/' + zip_files[i]
        with open(csv_path, 'r') as csvfile:
            records_reader = csv.reader(csvfile, delimiter=',')
            next(records_reader, None)
            stats_final = process_file(records_reader, zip_files[i])
            csvfile.close()
        writing_queue.put(stats_final)
        os.remove(csv_path)
    return True


def write_stats_to_csv(writing_queue, save_path):
    """Write user in writing_queue to csv."""
    while True:
        # wait for result to appear in the queue
        stats = writing_queue.get()
        # if got signal 'kill' exit the loop
        if stats == 'kill':
            break

        csv_path = os.path.join(save_path, 'stats.csv')
        with open(csv_path, 'a') as csv:
            json.dump(stats, csv)
            csv.write('\n')
            csv.close()


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


#####################################
# main program                      #
#####################################


parser = configargparse.ArgumentParser(
    description='Generate statistics for OPAL raw dataset.')
parser.add_argument('--num_threads', type=int, required=True,
                    help='Number of threads to be used to create data.')
parser.add_argument('--data_path', required=True,
                    help='Data path where generated csv have to be saved.')
args = parser.parse_args()

fileDirectory = args.data_path

if __name__ == "__main__":

    # Prevent attempt to start a new process before the current process has finished its bootstrapping phase in Windows.
    if os.name == 'nt':
        mp.freeze_support()

    print("Starting...")
    start_time = time.time()

    # We check if a stats file already exists, if it exists we cancel the operation
    csv_path = os.path.join(args.data_path, 'stats.csv')
    if os.path.exists(csv_path):
        print("The stats file already exists. I am not overwriting it. Cancelling operations.")
        sys.exit()

    # set up parallel processing
    manager = mp.Manager()
    writing_queue = manager.Queue()
    jobs = []
    # additional 1 process is for which shouldn't take up much CPU power
    pool = mp.Pool(processes=args.num_threads + 1)
    pool.apply_async(write_stats_to_csv, (writing_queue, args.data_path))
    if os.path.exists(fileDirectory):
        filesName = [f for f in listdir(fileDirectory) if isfile(join(fileDirectory, f))]
        chunks = chunks(filesName, args.num_threads - 1)
        chunksList = list(chunks)
        for n in range(len(chunksList)):
            print(chunksList[n])
            jobs.append(pool.apply_async(
                process_day, (writing_queue, chunksList[n], fileDirectory)))

    # clean up parallel processing (close pool, wait for processes to
    # finish, kill writing_queue, wait for queue to be killed)
    pool.close()
    for job in jobs:
        job.get()
    writing_queue.put('kill')
    pool.join()
    elapsed_time = time.time() - start_time
    print("The threads are done and it took: %f" % (elapsed_time))
