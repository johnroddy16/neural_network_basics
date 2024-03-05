# notes from the quiz:

import numpy as np

# a = np.random.randn(1,3)

# b = np.random.randn(3,3)

# c = a * b  

# print(c, c.shape)


# a = np.array([[2,1], [1,3]])
# b = np.dot(a,a)
# print(b)


a = np.array([[1,1], [1,-1]])
b = np.array([[2], [3]])
c = a + b 
print(c, c.shape)


# vectorization:

# a = np.random.randn(3, 4)
# b = np.random.randn(4,1)

# c = np.dot(a,b)
# print(c, c.shape)



# a = np.random.randn(3,3)

# b = np.random.randn(3,1)

# c = a * b

# print(c, c.shape)

# x = -(0.9 * np.log(1) + (1 - 0.9) * np.log(1 - 1))
# print(x)