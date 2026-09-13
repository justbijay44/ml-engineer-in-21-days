from pathlib import Path

import torch
from torch.utils.data import DataLoader

import torchvision
from torchvision.datasets import MNIST

from train import MnistNet

if __name__ == "__main__":
    data_dir = Path(__file__).parent.parent / "data"
    data_dir.mkdir(exist_ok=True)

    model = MnistNet(hidden=128)
    state_dict = torch.load(Path(__file__).parent / "models" / "model.pth")
    model.load_state_dict(state_dict)

    with torch.no_grad():
        test_data = MNIST(root=data_dir, train=False, download=True, transform=torchvision.transforms.ToTensor())

        test_loader = DataLoader(test_data, batch_size=64)

        correct, total = 0, 0

        for image, label in test_loader:
            prediction = model(image)
            predicted = torch.argmax(prediction, dim=1)

            correct += (predicted == label).sum().item()
            total += label.size(0)

        print(f"Accuray: {(correct / total) * 100} % ")