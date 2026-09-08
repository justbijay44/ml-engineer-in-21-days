import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def predict(X, weight, bias):
    return sigmoid(np.dot(X, weight) + bias)

def loss(y_true, y_pred):
    return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

def gradient(X, y_true, y_pred):
    dw = np.dot(X.T, (y_pred - y_true)) / len(y_true)
    db = np.mean(y_pred - y_true)
    return dw, db

if __name__ == "__main__":
    class_zero = np.random.randn(50, 2) + [2, 2]
    class_one = np.random.randn(50, 2) + [8, 8]

    labels_zero = np.zeros(50)
    labels_one = np.ones(50)

    X = np.vstack([class_zero, class_one])
    y = np.concatenate([labels_zero, labels_one])

    bias = 0
    weight = np.zeros(2)
    learning_rate = 0.1

    for idx in range(2000):
        y_pred = predict(X, weight, bias)

        loss_ = loss(y, y_pred)

        dw, db = gradient(X, y, y_pred)

        weight = weight - learning_rate * dw
        bias = bias - learning_rate * db

        if idx % 200 == 0:
            print(loss_)

    print(f"Weight:{weight} | Bias: {bias}")

    X_vals = np.linspace(X[:, 0].min(), X[:, 0].max(), 100)
    y_vals = -(weight[0] * X_vals + bias) / weight[1]

    plt.scatter(X[:,0], X[:,1], c=y)
    plt.plot(X_vals, y_vals, color='red')
    plt.show()