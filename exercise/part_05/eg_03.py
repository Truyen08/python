import numpy as np

#example of 2D array
arr2d = np.array([[1, 2, 3], 
                [4, 5, 6]])

print(arr2d)
element_1_2 = arr2d[0, 1]       #row 0, column 1
print("\n", element_1_2)

slice_arr2d = arr2d[1:3 , 1:]  #rows 1 to 2, columns 1 to end
print("slice_arr2d:\n", slice_arr2d)

print("-" * 20)
new_array2D = np.reshape(arr2d, (3, 2)) 
print(new_array2D) # Transpose the array