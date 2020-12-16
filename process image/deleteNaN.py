#!/usr/bin/env 
import pandas as pd

data = pd.read_csv('DEMdelete.txt', sep=' ', error_bad_lines=False, engine='python')
print(data.shape) 