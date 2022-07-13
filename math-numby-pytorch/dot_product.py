import numpy as np
import torch 

#  Using numpy
nv1 = np.array([1,2,3,4])
nv2 = np.array([0,1,-1,-2])
#  via function
print(np.dot(nv1, nv2))
# via basic computation
print(np.sum(nv1 * nv2))

#  Using touch
tv1 = torch.tensor([1,2,3,4])
tv2 = torch.tensor([0,1,-1,-2])
print(torch.dot(tv1, tv2))
print(torch.sum(tv1 * tv2))

