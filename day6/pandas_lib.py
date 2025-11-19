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
data2 = pd.Series(["C++","Java","Python"], index = list("CJP"),

name = "seri_example2")
print(data1)
print(data2)