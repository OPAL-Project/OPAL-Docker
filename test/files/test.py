#! python
import sys
import time

retrieve_params = sys.argv[1] + '\n'

# We add a sleep to be able to test that the job is running
time.sleep(20)

with open('output/test_out.txt', 'w') as f:
    f.write('Hello World !\n')
    print('Hello World !')
    f.write(retrieve_params)
    with open('faust.txt', 'r') as f2:
        for i in range(0, 10):
            line = f2.read()
            f.write(line)
    f.close()
