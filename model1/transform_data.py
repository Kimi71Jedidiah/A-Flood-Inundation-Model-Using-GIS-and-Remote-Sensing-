#!/usr/bin/env 
import pandas as pd

data = pd.read_csv('DEMdelete.txt', sep=' ', error_bad_lines=False, engine='python')
for col in data.columns:
    val = data[col].mean()
    data[col] = data[col].replace(0, 9999)
data.to_csv("DEM9999.txt", header=None, index=None, sep=' ', mode='a')