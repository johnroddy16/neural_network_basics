# broadcasting in python:

# say we have structured data as such:

'''
this is a comment i think, anyway:

        Apples    Beef    Eggs    Potatoes
Carb      56.0     0.0     4.4        68.0
Protein    1.2    104.0   52.0         8.0
Fat        1.8    135.0   99.0         0.9  (calories from each in 100 grams of the food)

'''

# we would like to find out the total calories for each food and what percentage of the calories are from carbs:
# we can create a A = (3, 4) matrix and use python code:

# here we go:

import numpy as np

A = np.array([[56.0, 0.0, 4.4, 68.0],
              [1.2, 104.0, 52.0, 8.0],
              [1.8, 135.0, 99.0, 0.9]])

print(A)

apples = []
beef = []
eggs = []
potatoes = []

# kount = 0 

x = A.shape[0]  # 3
y = A.shape[1]  # 4 
print(x, y)  # 3 4 

for i in range(x):
    for j in range(y):
        if j == 0:
            apples.append(A[i][j])
        elif j == 1:
            beef.append(A[i][j])
        elif j == 2:
            eggs.append(A[i][j])
        else:
            potatoes.append(A[i][j])

print(apples)  # [56.0, 1.2, 1.8]

print(f'apple calories: {sum(apples)}, percentage of calories from carbs: {100*(apples[0]/sum(apples)):.4f} %')

print('%.3f' % 3.14159)          # Prints 3.142
print('%.2f' % 3.141592653589)  # prints 3.14 

a = 10.1234
print(f'{a:.2f}')  # 10.12 



# now let us do that with broadcasting and 2 lines of python code:

cal = A.sum(axis=0)  # axis=0 means sum vertically, axis=1 will sum horizontally 
print(cal, cal.shape)  # [ 59.  239.  155.4  76.9] shape: (4,)   total calories for each food 

precentage = 100 * A/cal.reshape(1,4)  # this is an example of python broadcasting, where we divide a 3 x 4 matrix by a 1 x 4 matrix  
# the reshape is to create a matrix for broadcasting, reshape is not necessary in this example, does not hurt to use it anyway, sometimes needed, cheap to call so call it O(1)
# [[94.91525424  0.          2.83140283 88.42652796]
#  [ 2.03389831 43.51464435 33.46203346 10.40312094]
#  [ 3.05084746 56.48535565 63.70656371  1.17035111]]

print(precentage)

# see i need space for details on the matrix calculation 

cals = cal.reshape(1,4)
print(cals)  # [[ 59.  239.  155.4  76.9]]

