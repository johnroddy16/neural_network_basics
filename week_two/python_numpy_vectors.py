# notes on python and numpy vectors:

import numpy as np

a = np.random.randn(5)  # will create a rank 1 array of 5 gaussian variables 
print(a)  # [ -0.84649103 -0.23283501  0.76405219 -0.39270554 -0.661679  ] rank 1 array so one set of brackets
print(a.shape)  # (5,) rank 1 array, not a column or a row vector 

# if we attempt to transpose we will get the same array:
print(a.T)  # same as line 6 

# when creating neural networks it is best to avoid rank 1 arrays with shape (m,)

# instead:

a = np.random.randn(5,1)
print(a)  # we now have a (5,1) column vector
# [[-1.45471337]
#  [ 0.55090868]
#  [-1.73214348]
#  [ 1.32937868]
#  [ 1.35597174]]

# so now when we transpose we get what we would expect:
print(a.T)  # [[-0.61781891  0.81207592 -1.82183321 -1.07918011  0.67453092]] we now get a row vector
print(a.shape, a.T.shape)  # (5, 1) (1, 5)

# now np.dot(a,a.T) will return a (5,5) matrix instead of a scalar like it did before
