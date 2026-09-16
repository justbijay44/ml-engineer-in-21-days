from pathlib import Path

import torch
from torch import nn, optim
from torch.utils.data import DataLoader

from torchvision import transforms
from torchvision.datasets import CIFAR10

class CifarNet(nn.Module):
    def __init__(self, hidden):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3)
        self.conv3 = nn.Conv2d(32, 64, kernel_size=3)

        self.maxpool = nn.MaxPool2d(2)

        self.bn1 = nn.BatchNorm2d(16)
        self.bn2 = nn.BatchNorm2d(32)
        self.bn3 = nn.BatchNorm2d(64)

        self.dropout = nn.Dropout(0.3)

        self.fc1 = nn.Linear(1024, hidden)
        self.fc2 = nn.Linear(hidden, 10)

    def forward(self, x):
        x = self.maxpool(torch.relu(self.bn1(self.conv1(x))))
        x = self.maxpool(torch.relu(self.bn2(self.conv2(x))))
        x = torch.relu(self.bn3(self.conv3(x)))

        x = torch.flatten(x, 1)

        x = self.dropout(torch.relu(self.fc1(x)))
        x = self.fc2(x)

        return x

if __name__ == "__main__":
    
    data_dir = Path(__file__).parent.parent / "DAY_13" / "data"
    model_dir = Path(__file__).parent / "models"

    data_dir.mkdir(exist_ok=True)
    model_dir.mkdir(exist_ok=True)

    torch.manual_seed(42)

    transform = transforms.Compose([
        transforms.RandomHorizontalFlip(),
        transforms.RandomCrop(32, padding=4),
        transforms.ToTensor()
    ])

    train_data = CIFAR10(data_dir, train=True, download=True,
                        transform=transform)

    train_loader = DataLoader(train_data, batch_size=64, shuffle=True)

    test_data = CIFAR10(data_dir, train=False, download=True, transform=transforms.ToTensor())
    test_loader = DataLoader(test_data, batch_size=64)
    
    criterion = nn.CrossEntropyLoss()

    model = CifarNet(hidden=128)

    optimizer = optim.Adam(model.parameters(), lr=0.001)

    best_acc = 0
    for epoch in range(80):
        for image, label in train_loader:
            predict = model(image)

            loss = criterion(predict, label)

            optimizer.zero_grad()

            loss.backward()

            optimizer.step()


        if epoch % 5 == 0:
            model.eval()

            correct, total = 0, 0
            with torch.no_grad():
                for image, label in test_loader:
                    predicted = torch.argmax(model(image), dim=1)

                    correct += (predicted == label).sum().item()
                    total += label.size(0)
            acc = correct/total
            if acc > best_acc:
                torch.save(model.state_dict(), model_dir / "model.pth")
                best_acc = acc

            print(f"epoch {epoch} | loss: {loss.item():.4f} | test acc: {correct/total*100:.2f}%")
            model.train()
