from pathlib import Path

import torch
from train import CifarNet

import torchvision
from torchvision.datasets import CIFAR10

model = CifarNet(hidden=128)
state_dict = torch.load(Path(__file__).parent / "models" / "model.pth")
model.load_state_dict(state_dict)

def predict_image(image):
    image = image.unsqueeze(0)
    with torch.no_grad():
        output = model(image)
    predicted = torch.argmax(output, dim=1)
    return predicted.item()

if __name__ == "__main__":
    test_data = CIFAR10(Path(__file__).parent / "data", train=False, download=True, transform=torchvision.transforms.ToTensor())
    image, true_label = test_data[0]
    predicted = predict_image(image)
    print(test_data.classes[predicted], test_data.classes[true_label])
