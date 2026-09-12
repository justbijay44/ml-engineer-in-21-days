import torch
from torch import nn, optim

import numpy as np

class XorNet(nn.Module):
    def __init__(self, hidden_size):
        super().__init__()
        self.layer1 = nn.Linear(2, hidden_size)
        self.layer2 = nn.Linear(hidden_size, 1)

    def forward(self, x):
        a1 = torch.sigmoid(self.layer1(x))
        out = torch.sigmoid(self.layer2(a1))
        return out


if __name__ == "__main__":
    X = np.array([[0,0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 1, 1, 0])

    X = torch.tensor(X, dtype=torch.float32)
    y = torch.tensor(y, dtype=torch.float32)
    y = y.reshape(-1, 1)

    model = XorNet(4)

    optimizer = optim.Adam(model.parameters(), lr=0.01)

    criterion = nn.BCELoss()            # gives binarycross entropy
    
    for idx in range(1000):

        prediction = model(X)

        loss = criterion(prediction, y)

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()

        if idx % 200 == 0:
            print(loss.item())

    print(model(X))