import numpy as np
import matplotlib.pyplot as plt

def random_x_y():
    noise_scale = 1
    x = np.random.rand(50) * 10
    y = 3 * x + 5 + np.random.randn(50) * noise_scale
    return x, y

def predict(x, m, c):
    return m * x + c

def loss(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

def gradient(x, y, y_pred):
    dm = -2 * np.mean(x * (y - y_pred))
    dc = -2 * np.mean(y - y_pred)

    return dm, dc

if __name__ == "__main__":
    m, c = 0, 0
    x, y = random_x_y()
    learning_rate = 0.001


    for idx in range(5000):
        # pred
        y_pred = predict(x, m, c)

        # get loss and repeat
        loss_ = loss(y, y_pred)

        # calculate grad
        dm, dc = gradient(x, y, y_pred)

        # update
        m = m - learning_rate * dm
        c = c - learning_rate * dc

        if idx % 100 == 0:
            print(loss_)

    print(f"M:{m} | C: {c}")

    plt.scatter(x, y)
    plt.plot(x, predict(x, m, c), color='red')
    plt.show()