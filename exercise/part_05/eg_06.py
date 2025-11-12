import numpy as np
original_array1 = np.array([[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9]])

original_array2 = np.array([[10, 20, 30],
                            [40, 50, 60],
                            [70, 80, 90]])


new_array1 = np.append(original_array1, original_array2, axis=1)
print("new_array1:\n", new_array1)
new_array2 = np.append(original_array1, original_array2, axis=0)
print("new_array2:\n", new_array2)  