#  Numpy Arithmetic Operations
import numpy as np
a = np.array ([[0, 3, 1],
			 [3, 7, 5],
 			[6, 4, 8]])
b = [10, 5, 11]

print("add_array =\n",np.add(a,b))
print("subtract_array =\n",np.subtract(a,b))
print("multiply_array =\n",np.multiply(a,b))
print("divide_array =\n",np.divide(a,b))

print("--"*20)
print("sum_a =",np.sum(a))	#total sum of all elements in a
print("sum_b =",np.sum(b))	#total sum of all elements in b

print("sum of each column in a =",np.sum(a, axis=0)) #sum of each column
print("sum of each row in a =",np.sum(a, axis=1)) #sum of each row