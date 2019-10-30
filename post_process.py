import pandas as pd
import glob 
li = []
for file in glob.glob("output/house_hvac_load"+"*.csv") :
	print(file)
	df = pd.read_csv(file, index_col=None, header=0)
# 	li.append(df)
# frame = pd.concat(li, axis=0, ignore_index=True)
	# print(df)
