#!/usr/bin/env 
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

data = pd.read_csv('res_3e8_norain.txt', delim_whitespace=True, error_bad_lines=False, engine='python')
# data = pd.read_csv('res_3e8_norain.totaltm', sep=' ', error_bad_lines=False, engine='python')

r = 0
c = 0

width,height = data.shape
print(width, height)
npdata = np.zeros((height,width,3))  
#print(data)
maxdata = 0.0

for col in data.columns:
	c = 0
	for cell in data[col]:
		#print(cell)
		npdata[r,c,0] =float(cell)
		npdata[r,c,1] =float(cell)
		npdata[r,c,2] =float(cell)
		maxdata = max(float(cell),maxdata)
		c += 1
	r += 1


print(npdata[3])
img = Image.fromarray(npdata, 'RGB')
img.save("norain_8e3.png")
img.show()


