import numpy as np

a = np.zeros((3,3))
print(a)

np.fill_diagonal(a, [1,2,3])
print(a)