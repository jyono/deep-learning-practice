#  Transpose vector and matrices
import numpy as np
import torch

# Using numpy
# Transpose a vector
nv = np.array([1, 2, 3, 4, 5])
print(nv)
print(' ')
# .T is syntax sugar for a transpose
print(nv.T), print()


# Transpose a matrix
nv = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])
print(nv)
print(' ')
print(nv.T)


# Using pytorch
# Transpose a vector
tv = torch.tensor([
    [1, 2, 3, 4]
])
print(tv)
print(' ')
print(tv.T)

# Transpose a matrix
tv = torch.tensor([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])
print(tv)
print(' ')
print(tv.T)
