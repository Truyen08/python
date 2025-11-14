#first you need to install lib by this command:"pip install numpy"
import numpy as np

arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

slice_arr2d = arr2d[1:3, 1:]
print("arr2d:\n", arr2d)

print("\n", slice_arr2d)        # rows 1 to 2, columns 1 to end

print("-" * 20)
new_array_01 = arr2d.transpose()   # Transpose the array
print(new_array_01)

#``````````````````````````````````````````````
print("-" * 20)
new_array_02 = np.reshape(arr2d, (9, 1))  
new_array_02 = np.reshape(arr2d, (1, 9))  # Reshape to 1 row and 9 columns
print(new_array_02)

print("-" * 20)
new_array_03 = np.resize(arr2d, (2, 2))   # Resize the original array to 5 rows and 2 columns
print(new_array_03)


'''
    the difference between reshape and resize:
    - reshape: returns a new array with the specified shape, without changing the original array.
    - resize: changes the shape of the original array in place (may lose data).
'''

#````````````````````````````````````````````````

