import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
th = x[x%3==0]
print(th)
fo = x[x%4 == 1]
print(fo)
cc = x[(x%3 == 0) & (x%4 == 1)]
print(cc)