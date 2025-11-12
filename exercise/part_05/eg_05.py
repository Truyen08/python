import numpy as np


#axis=0  is rows
#axis=1  is columns

original_array = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]])
new_array1 = np.delete(original_array,0,axis=0)
new_array2 = np.delete(original_array,0,axis=1)
new_array3 = np.delete(original_array,2,axis=0)
new_array4 = np.delete(original_array,2,axis=1)