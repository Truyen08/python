import numpy as np

arr_2D = np.array([[1 , 2, 3], 
                    [4, 5, 6]])

# (2, 3) ->(3, 2)
new_arr_2D = np.reshape(arr_2D , (3, 2))

# 2D -> 1D
arr_1D = np.reshape(arr_2D , newshape =(6 , ))


print("array 2D:\n", arr_2D , arr_2D.shape )        
#array.shape: it means the shape of the array

print("new array 2D :\n", new_arr_2D, new_arr_2D.shape)

print("array 1D:\n", arr_1D, arr_1D.shape)


print("-" * 20)
#arr_2D.resize(5, 2)         #Use this case when "resize" returns the array on the spot (not recommended)
new_arr = np.resize(arr_2D, (5, 2))   # Resize the original array to 5 rows and 2 columns
print(new_arr)


