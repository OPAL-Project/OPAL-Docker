import os
import json
import pandas as pd


data_path = ''
file_path = os.path.join(data_path, 'stats_senegal.json')

# we process the stats file
lines = [json.loads(str(line.rstrip('\n'))) for line in open(file_path)]

# We convert to a panda dataframe
data_frame = pd.DataFrame(lines)

print(list(data_frame.columns.values))

print(data_frame)

unvalide_field = data_frame.loc[data_frame["NotWellFormedWrongNumberFormat"]>0]

print(unvalide_field["NotWellFormedWrongNumberFormat"])
