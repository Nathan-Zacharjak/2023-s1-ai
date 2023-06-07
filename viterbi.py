import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([7, 8, 9])
maps = [a,b,c]

np.savez("output.npz", *maps)
print(maps)