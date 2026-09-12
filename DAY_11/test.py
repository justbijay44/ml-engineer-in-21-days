import torch
import numpy as np

def random_x_y():
    noise = 1
    x = np.random.rand(50) * 10
    y = 3 * x + 5 + np.random.randn(50) * noise

    x = torch.tensor(x, dtype=torch.float32)
    y = torch.tensor(y, dtype=torch.float32)
    return x, y

def calc_loss(y_true, y_pred):
    return ((y_true - y_pred) ** 2).mean()

def predict(x, m, c):
    return m * x + c


if __name__ == "__main__":
    learning_rate = 0.01
    m = torch.tensor(0.0, requires_grad=True)
    c = torch.tensor(0.0, requires_grad=True)

    x, y = random_x_y()

    for idx in range(1000):
        prediction = predict(x, m, c)
        loss = calc_loss(y, prediction)
        loss.backward()

        with torch.no_grad():
            m -= learning_rate * m.grad
            c -= learning_rate * c.grad

            m.grad.zero_()
            c.grad.zero_()

        if idx % 100 == 0:
            print(loss)

    print(m, c)