import torch
from torch import nn, optim

import numpy as np

class LinearRegression(nn.Module):
    def __init__(self):
        super().__init__()

        self.m = nn.Parameter(torch.tensor(0.0))
        self.c = nn.Parameter(torch.tensor(0.0))

    def forward(self, x):
        return self.m * x + self.c

    def calc_loss(self, y, x):
        y_pred = self.forward(x)
        return ((y - y_pred) ** 2).mean()

def random_x_y():
    noise = 1
    x = np.random.rand(50) * 10
    y = 3 * x + 5 + np.random.randn(50) * noise

    x = torch.tensor(x, dtype=torch.float32)
    y = torch.tensor(y, dtype=torch.float32)

    return x, y
    
if __name__ == "__main__":
    model = LinearRegression()
    x, y = random_x_y()

    optimizer = optim.SGD(model.parameters(), lr=0.01)
    for idx in range(1000):
        predict = model.forward(x)

        loss = model.calc_loss(y, x)

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()

        if idx % 200 == 0:
            print(loss.item())

    print(model.m.item(), model.c.item())