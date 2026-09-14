from pathlib import Path

import torch
from torch import nn, optim
from torch.utils.data import DataLoader

import torchvision
from torchvision.datasets import CIFAR10

class CifarNet(nn.Module):
    def __init__(self, hidden):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3)
        self.pool = nn.MaxPool2d(2)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3)
        self.fc1 = nn.Linear(1152, hidden)
        self.fc2 = nn.Linear(hidden, 10)

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = self.pool(torch.relu(self.conv2(x)))

        x = torch.flatten(x, 1)

        x = torch.relu(self.fc1(x))
        x = self.fc2(x)

        return x

if __name__ == "__main__":
    data_dir = Path(__file__).parent / "data"
    model_dir = Path(__file__).parent / "models"

    data_dir.mkdir(exist_ok=True)
    model_dir.mkdir(exist_ok=True)

    train_data = CIFAR10(data_dir, train=True, download=True, 
                        transform=torchvision.transforms.ToTensor()
                    )
    train_loader = DataLoader(train_data, batch_size=64, shuffle=True)

    model = CifarNet(hidden=128)

    criterion = nn.CrossEntropyLoss()

    optimizer = optim.Adam(model.parameters(), lr=0.001)

    for epoch in range(10):
        for image, label in train_loader:
            predict = model(image)

            loss = criterion(predict, label)

            optimizer.zero_grad()

            loss.backward()

            optimizer.step()

        if epoch % 2 == 0:
            print(loss.item())

    torch.save(model.state_dict(), model_dir / 'model.pth')