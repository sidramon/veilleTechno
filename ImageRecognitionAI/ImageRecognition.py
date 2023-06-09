from PIL import Image, ImageTk
from torchvision import models, transforms
import torch


# ImageRecognition Class #
class ImageRecognition:
    def __init__(self):
        # Load model
        self.model = models.resnet101(pretrained=True)
        self.model.eval()

        # Set image transform
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])

        # Load classes
        self.labels = open("models/imagenet_classes.txt").read().splitlines()

    def recognize_image(self, image):
        # Convert and transform image
        image_pil = ImageTk.getimage(image).resize((224, 224), Image.BILINEAR).convert('RGB')
        image_tensor = self.transform(image_pil)
        image_tensor = image_tensor.unsqueeze(0)

        # predict image
        with torch.no_grad():
            predictions = self.model(image_tensor)
            _, predicted_idx = torch.max(predictions, 1)
        predicted_label = self.labels[predicted_idx.item()]

        return predicted_label
