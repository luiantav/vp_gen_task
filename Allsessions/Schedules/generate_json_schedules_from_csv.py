import pandas as pd
import json

input_file = "schedule.csv"
output_file = "schedule"

# read file and dump as raw json without assignment
df = pd.read_csv(input_file).set_index("SubID", drop=False)
df.to_json(output_file+".json", orient="index")

# append the name of the variable and apostrophes
f = open(output_file+".json", "r+")
js = f.read()
f.seek(0,0)
f.write("data='" + js + "'")
f.close()
