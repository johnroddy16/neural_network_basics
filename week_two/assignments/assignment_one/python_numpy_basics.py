# notes and graded functions from assignment one, python and numpy basics:

# excercise 2:

import math

import numpy as np 


# GRADED FUNCTION: basic_sigmoid

def basic_sigmoid(x):
    """
    Compute sigmoid of x.

    Arguments:
    x -- A scalar

    Return:
    s -- sigmoid(x)
    """
    # (≈ 1 line of code)
    # s = 
    # YOUR CODE STARTS HERE
    
    s = 1 / (1 + math.exp(-x))
    
    # YOUR CODE ENDS HERE
    
    return s

print(basic_sigmoid(4)) 

# All tests passed. 



# exercise 3:

# GRADED FUNCTION: sigmoid

def sigmoid(x):
    """
    Compute the sigmoid of x

    Arguments:
    x -- A scalar or numpy array of any size

    Return:
    s -- sigmoid(x)
    """
    
    # (≈ 1 line of code)
    # s = 
    # YOUR CODE STARTS HERE
    
    s = 1 / (1 + np.exp(-x))
    
    # YOUR CODE ENDS HERE
    
    return s

# All tests passed.

# exercise 4 - sigmoid derivative:

def sigmoid_derivative(x):
    """
    Compute the gradient (also called the slope or derivative) of the sigmoid function with respect to its input x.
    You can store the output of the sigmoid function into variables and then use it to calculate the gradient.
    
    Arguments:
    x -- A scalar or numpy array

    Return:
    ds -- Your computed gradient.
    """
    
    #(≈ 2 lines of code)
    # s = 
    # ds = 
    # YOUR CODE STARTS HERE
    
    s = sigmoid(x)
    ds = s * (1 - s)
    
    # YOUR CODE ENDS HERE
    
    return ds



# excersise 5 - image2vector:

def image2vector(image):
    """
    Argument:
    image -- a numpy array of shape (length, height, depth)
    
    Returns:
    v -- a vector of shape (length*height*depth, 1)
    """
    
    # (≈ 1 line of code)
    # v =
    # YOUR CODE STARTS HERE
    
    v = image.reshape((image.shape[0] * image.shape[1] * image.shape[2], 1))
    
    # YOUR CODE ENDS HERE
    
    return v

#  All tests passed.



# exercise 6 - normalize_rows:

# GRADED FUNCTION: normalize_rows

def normalize_rows(x):
    """
    Implement a function that normalizes each row of the matrix x (to have unit length).
    
    Argument:
    x -- A numpy matrix of shape (n, m)
    
    Returns:
    x -- The normalized (by row) numpy matrix. You are allowed to modify x.
    """
    
    #(≈ 2 lines of code)
    # Compute x_norm as the norm 2 of x. Use np.linalg.norm(..., ord = 2, axis = ..., keepdims = True)
    # x_norm =
    # Divide x by its norm.
    # x =
    # YOUR CODE STARTS HERE
    
    x_norm = np.linalg.norm(x, ord=2, axis=1, keepdims=True)
    
    x = (x / x_norm)
    
    # YOUR CODE ENDS HERE

    return x, x.shape, x_norm.shape 

# ll tests passed.



x = np.array([[0., 3., 4.],
              [1., 6., 4.]])
print("normalizeRows(x) = " + str(normalize_rows(x)))



# exercise 7 - softmax:

# GRADED FUNCTION: softmax

def softmax(x):
    """Calculates the softmax for each row of the input x.

    Your code should work for a row vector and also for matrices of shape (m,n).

    Argument:
    x -- A numpy matrix of shape (m,n)

    Returns:
    s -- A numpy matrix equal to the softmax of x, of shape (m,n)
    """
    
    #(≈ 3 lines of code)
    # Apply exp() element-wise to x. Use np.exp(...).
    # x_exp = ...

    # Create a vector x_sum that sums each row of x_exp. Use np.sum(..., axis = 1, keepdims = True).
    # x_sum = ...
    
    # Compute softmax(x) by dividing x_exp by x_sum. It should automatically use numpy broadcasting.
    # s = ...
    
    # YOUR CODE STARTS HERE
    
    x_exp = np.exp(x)
    
    x_sum = np.sum(x_exp, axis=1, keepdims=True)
    
    s = x_exp / x_sum 
    
    # YOUR CODE ENDS HERE
    
    return s

print()

t_x = np.array([[9, 2, 5, 0, 0],
                [7, 5, 0, 0 ,0]])

x_exp = np.exp(t_x)
print(x_exp)

print()

x_sum = np.sum(x_exp, axis=1, keepdims=True)
print(x_sum)

print()

s = x_exp / x_sum
print(s)

# All tests passed.



# exercise 8 - L1:

yhat = np.array([.9, 0.2, 0.1, .4, .9])
y = np.array([1, 0, 0, 1, 1])

loss = np.sum(np.abs(yhat - y)) 
print()
print(loss)

# GRADED FUNCTION: L1

def L1(yhat, y):
    """
    Arguments:
    yhat -- vector of size m (predicted labels)
    y -- vector of size m (true labels)
    
    Returns:
    loss -- the value of the L1 loss function defined above
    """
    
    #(≈ 1 line of code)
    # loss = 
    # YOUR CODE STARTS HERE
    
    loss = np.sum(np.abs(yhat - y))
    
    # YOUR CODE ENDS HERE
    
    return loss

# All tests passed.



# exercise 9 - L2:

# GRADED FUNCTION: L2

def L2(yhat, y):
    """
    Arguments:
    yhat -- vector of size m (predicted labels)
    y -- vector of size m (true labels)
    
    Returns:
    loss -- the value of the L2 loss function defined above
    """
    
    #(≈ 1 line of code)
    # loss = ...
    # YOUR CODE STARTS HERE
    
    loss = np.sum((y - yhat) ** 2)
    
    # YOUR CODE ENDS HERE
    
    return loss

print() 

yhat = np.array([.9, 0.2, 0.1, .4, .9])
y = np.array([1, 0, 0, 1, 1])

print("L2 = " + str(L2(yhat, y)))

# All tests passed. 