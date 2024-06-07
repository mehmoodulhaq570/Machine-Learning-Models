import numpy as np

def Gradient_Descent(x,y):
    
    #Initializes the parameters m_curr (slope) and b_curr (intercept) to zero. These parameters will be updated during the gradient descent process.
    m_curr = b_curr = 0 
    iterations = 5000
    n = len(x)

    # The learning rate is a crucial hyperparameter used in optimization algorithms like gradient descent. 
    # It determines the size of the steps taken towards minimizing the loss function (or error)
    # The smaller the learning rate, the slower the algorithm will converge, but it will get closer to the optimal values.
    learning_rate = 0.08
    
    for i in range(iterations):

        # Here is the formula we have learned previously in linear regression y = m*x + b
        y_predicted = m_curr * x + b_curr

        # This is the mathematical formula of cost function or Mean square error (MAE) 
        cost = (1/n)*sum([val**2 for val in (y-y_predicted)])
        md = -(2/len(x)) * sum(x * (y - y_predicted))
        bd = -(2/len(x)) * sum(y - y_predicted)

        # Updates the parameter m_curr by subtracting the product of the learning rate and the gradient with respect to m. 
        # This step moves m_curr in the direction that reduces the error.
        m_curr = m_curr - learning_rate*md

        # Updates the parameter b_curr by subtracting the product of the learning rate and the gradient with respect to b.
        # This step moves b_curr in the direction that reduces the error.
        b_curr = b_curr - learning_rate*bd

        # Prints the current values of m_curr and b_curr and the current value of the cost function.
        #The {} in the string "m {}, b {}, cost {}, iterations{}" are placeholders used for string formatting.
        # This approach allows dynamic insertion of variables into the string at runtime
        print("m {}, b {}, cost {}, iterations{}".format(m_curr, b_curr, cost, i))


# NumPy arrays are implemented in C and are much faster than Python lists, especially for numerical computations. 
# Operations on NumPy arrays are vectorized, meaning they are applied to entire arrays at once, which can lead to significant speedups.
x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

Gradient_Descent(x,y)