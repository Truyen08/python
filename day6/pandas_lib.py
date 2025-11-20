# pip install pandas
# import pandas
#import pandas as pd

'''
in pandas has 3 main data structures:
1. Series: 1D array
2. DataFrame: 2D array
3. Panel: 3D array or more
'''
import pandas as pd

data1 = pd.Series([5,7,5,1,6], name = "seri_example1")
data2 = pd.Series(["C++","Java","Python", "NET"], index = list("CJPN"), name = "seri_example2")

print(data1)
print(data2)




print("--"*20)
print(data1[0])
print(data1[3]) 

data1[2.5] = 9  #add new value at index 2.5

data1.sort_index(inplace=True)  #sort index

data1.reset_index(drop=True)  #reset index
print(data1)




print("--"*20)
print(data1[2:4])  #print value from index 2 to 3




print(data2["J"])

print(data2.str.count('a'))
print(data2.str.count('Python'))

print(data2.str.upper())
print(data2.str.replace("Java", "C#"))