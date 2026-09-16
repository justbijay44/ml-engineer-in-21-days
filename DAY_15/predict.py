from pathlib import Path

import torch
from torch import nn, optim
from torch.utils.data import DataLoader

import torchvision
from torchvision import transforms
from torchvision.datasets import CIFAR10

from train import CifarNet

if __name__ == "__main__":
    data_dir = Path(__file__).parent.parent / "DAY_13" / "data"

    model = CifarNet(hidden=128)
    state_dict = torch.load("models/model.pth")
    model.load_state_dict(state_dict)
    
    model.eval()

    test_data = CIFAR10(data_dir, train=False, download=True, transform=transforms.ToTensor())
    test_loader = DataLoader(test_data, batch_size=64)

    correct, total = 0, 0

    with torch.no_grad():
        for image, label in test_loader:
            predict = model(image)
            predicted = torch.argmax(predict, dim=1)

            correct += (predicted == label).sum().item()
            total += label.size(0)

        print(f"Accuracy: {(correct / total) * 100:.2f} % ")
    