import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def forward(X, W1, b1, W2, b2):
    z1 = np.dot(X, W1) + b1
    a1 = sigmoid(z1)            # output of hidden layer

    z2 = np.dot(a1, W2) + b2
    a2 = sigmoid(z2)            # final op

    return a1, a2

def loss(y_true, y_pred):
    return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

def backward(X, y, a1, a2, W2):
    m = len(y)
    dz2 = a2 - y.reshape(-1, 1)         # how wrong was the pred.
    dW2 = np.dot(a1.T, dz2) / m         # output weight changes for W2
    db2 = np.mean(dz2, axis=0)          # change in b2

    da1 = np.dot(dz2, W2.T)             # error from hidden layer
    dz1 = da1 * a1 * (1 - a1)           # account for activation func effect
    dW1 = np.dot(X.T, dz1) / m          # output weight changes for W1
    db1 = np.mean(dz1, axis=0)          # changes for b1

    return dW1, db1, dW2, db2

if __name__ == "__main__":
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]]) 
    y = np.array([0, 1, 1, 0])

    plt.scatter(X[:, 0], X[:, 1], c=y)
    # plt.show()

    np.random.seed(0)
    learning_rate = 0.5
    
    # weight and bias for input
    W1 = np.random.randn(2, 8)
    b1 = np.zeros(8)

    # weight and bias for neurons
    W2 = np.random.randn(8, 1)
    b2 = np.zeros(1)


    for idx in range(20000):
        # forward pass
        a1, a2 = forward(X, W1, b1, W2, b2)

        # loss
        loss_ = loss(y, a2)

        # updates to make
        dW1, db1, dW2, db2 = backward(X, y, a1, a2, W2)

        W1 -= learning_rate * dW1
        b1 -= learning_rate * db1
        W2 -= learning_rate * dW2
        b2 -= learning_rate * db2

        if idx % 1000 == 0:
            print(loss_)