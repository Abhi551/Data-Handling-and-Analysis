## there are three different methods for slicing but only two are used more often
## 1. loc , get rows or columns with particular labels from the index
## 2. iloc  , get rows or columns with particular positions in the index

import pandas as pd 
import numpy as np


s = pd.Series(np.nan, index=[49,48,47,46,45, 1, 2, 3, 4, 5])
print (s.iloc[:3])
print (s.loc[:3])

print (s.iloc[:6])
try :
	print (s.loc[:6])
except :
	print ("6 not in the index ")

df = pd.read_csv('eg.csv')
df.set_index(['windspeed'] , inplace = True )
print (df)

print (df.iloc[:5])
try :
	print (df.loc[:5])
except :
	print ("5 not in index")