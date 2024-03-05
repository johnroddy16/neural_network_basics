# vectorization and python, course one week 2:

import numpy as np

import time 

# create 2 random vectors:

a = np.random.rand(100000)
b = np.random.rand(100000)

# time with vectorization:

tic = time.time()
c = np.dot(a,b)
toc = time.time()

print(c)
print('vectorized version:' + str(1000*(toc-tic)) + 'ms')

# time with a for loop:

c = 0
tic = time.time()
for i in range(100000):
    c += a[i] * b[i]
toc = time.time()

print(c)
print('for loop:' + str(1000*(toc-tic)) + 'ms')

# vectorized is ≈ 900 times faster on this computer 