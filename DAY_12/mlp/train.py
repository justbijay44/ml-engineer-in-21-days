from pathlib import Path

import torch
from torch import nn, optim
from torch.utils.data import DataLoader

import torchvision
from torchvision.datasets import MNIST

class MnistNet(nn.Module):
    def __init__(self, hidden):
        super().__init__()
        self.layer1 = nn.Linear(784, hidden)
        self.layer2 = nn.Linear(hidden, 10)

    def forward(self, x):
        x = torch.flatten(x, 1)
        x = torch.relu(self.layer1(x))
        x = self.layer2(x)
        return x

if __name__ == "__main__":
    data_dir = Path(__file__).parent.parent / "data"
    model_dir = Path(__file__).parent / "models"

    data_dir.mkdir(exist_ok=True)
    model_dir.mkdir(exist_ok=True)

    train_data = MNIST(root=data_dir, train=True, download=True, transform=torchvision.transforms.ToTensor())

    train_loader = DataLoader(train_data, batch_size=64, shuffle=True)

    model = MnistNet(hidden=128)

    criterion = nn.CrossEntropyLoss()

    optimizer = optim.Adam(model.parameters(), lr=0.001)

    epochs = 10
    for epoch in range(epochs):
        for image, label in train_loader:

            prediction = model(image)

            loss = criterion(prediction, label)

            optimizer.zero_grad()

            loss.backward()

            optimizer.step()

        if epoch % 2 == 0:
            print(loss.item())

    torch.save(model.state_dict(), model_dir / 'model.pth')

