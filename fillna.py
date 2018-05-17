import pandas  as pd 

data = pd.read_csv("eg.csv")

## check which values are NaN
print ("all those value which are True are NaN")
print (data.isna())
## printing only the 
df = pd.read_csv("eg.csv" , nrows = 0 )

## this gives the access to headers
print (df.columns)

## this works automatically for all data
## printing all data separately
for header in df.columns:
	print (data[header])

print (data)

## parsing date is helpful in handling dates
data =  pd.read_csv("eg.csv",parse_dates = ['day'])

## it is better to use index of our own
new_df =  data.set_index(["day"])
print (new_df)

## fillna method is used to fill NaN values in the dataframe
value  = input("Enter the value to filled = ")
new_df1 = new_df.fillna(int(value))
print (new_df1)

## filling na_values column-wise 

new_df1 =  new_df.fillna({"temprature" : 0 ,
							"windspeed" :  0 ,
							"event" : "no event"})
print (new_df1)

## fillna method provides different methods to fill NaN values 
## new_df.fillna(method = )

for methods in ["bfill" , "ffill" ]:
	##there are 2 ways in which data can be filled , i.e. 2 axis along which data can be filled 
	## axis = coloumn or row
	for axis in ["columns" , "rows"]:
		## limit option provides to how many next columns method is to be applied
		new_df1 =new_df.fillna(method =  methods , axis = axis , limit = 1)
		print ("\nmethod used is %s along %s" %(methods , axis))
		print (new_df1)

## using interpolation methods for handling the data


## there are different methods that can be applied on data
methods = ["linear" , "quadratic" ,  "cubic"  ,"spline"  , "time"]
for meth in methods:
	new_df1 = new_df
	print ("\n\nmethod used is %s \n" % meth )
	if meth == "spline":
		new_df1 = new_df1.interpolate(method = meth, order = 4)
	else :
		new_df1 = new_df1.interpolate(method = meth)
	print (new_df1)

## dropping the na_values , using dropna method

new_df1 =  new_df 
## thresh means how many non Nan values should be present 
new_df1.dropna(inplace = True , thresh = 1)
print(new_df1)
