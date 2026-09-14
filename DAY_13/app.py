import io
from PIL import Image

from fastapi import FastAPI, File, UploadFile

from torchvision import transforms

from inference import predict_image

app = FastAPI()

transform = transforms.Compose([
    transforms.Resize((32, 32)),
    transforms.ToTensor()
])

CIFAR10_CLASSES = ["airplane","automobile","bird","cat","deer","dog","frog","horse","ship","truck"]

@app.post("/predict")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    image = Image.open(io.BytesIO(content)).convert("RGB")
    image_tensor = transform(image)
    predicted = predict_image(image_tensor)
    return {"class": CIFAR10_CLASSES[predicted]}