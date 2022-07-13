import numpy as np
import torch

# Reminder for when matrix multiplication is valid...
#  for M1xN1 * M2xN2...
#  1. inner dimensions must match.
#       N1 must equal M2
#  2. outer dimensions dimensions of the resulting array
#       The result will be a M1xN2 matrix
#
# If it is valid, then we can fill in the result matrix with ordered dot products
# It is evident that rule 1 is true because we will be multiplying every number in the row by every number in the equivalent column
# It is evident that rule 2 must be true because when we will multiple every row by every column.

# So for a 2x2 matrix times another 2x2 matrix,
#
# [         *   [               [
#   0 1           a b               0a+1c 0b+1d
#   2 3           c d       =       2a+3c 2b+3d
# ]             ]               ]
#
#


# create some random matrices

a = np.random.randn(3, 4)
b = np.random.randn(4, 5)
c = np.random.randn(3, 7)
# a@b is syntax sugar for np.matmul(a,b) to multiply 2 matrices
print(np.round(a@b, 2))

# This will be undefined because aN != cM . The inner dimensions dont match :)
# print(np.round(a@c, 2))

# We can transpose c and then multiplu it by a.
# c = 3x7, thus c.T = 7x3
print(np.round(c.T@a, 2))


# Using torch
print("using torch")
a = torch.randn(3, 4)
b = torch.randn(4, 5)
c1 = np.random.rand(4, 7)
c2 = torch.tensor(c1, dtype=torch.float)

print(np.round(a@b, 2))
# Numpy and pytorch playing nice together :)
print(np.round(a@c1, 2))
