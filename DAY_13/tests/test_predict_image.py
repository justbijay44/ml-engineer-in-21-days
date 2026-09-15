import pytest

from torchvision.datasets import CIFAR10
from torchvision.transforms import transforms
from pathlib import Path

from inference import predict_image

@pytest.fixture
def test_image():
    test_data = CIFAR10(
            Path(__file__).parent.parent / "data",
            train=False,
            download=True,
            transform=transforms.ToTensor() 
        )
    image, _ = test_data[0]
    return image
    
def test_predict_image_return_type(test_image):
    result = predict_image(test_image)
    assert isinstance(result, int)

def test_predict_image_range(test_image):
    result = predict_image(test_image)
    assert 0 <= result <= 9