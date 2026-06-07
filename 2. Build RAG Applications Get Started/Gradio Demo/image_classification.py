import torch
import requests
from torchvision import transforms
import gradio as gr

model = torch.hub.load('pytorch/vision:v0.6.0', 'resnet18', pretrained=True).eval()

response = requests.get("https://git.io/JJkYN")
labels = [l.strip() for l in response.text.split("\n") if l.strip()]

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(
        [0.485, 0.456, 0.406],
        [0.229, 0.224, 0.225]
    )
])

def predict(inp):
    inp = transform(inp).unsqueeze(0)

    with torch.no_grad():
        prediction = torch.nn.functional.softmax(model(inp)[0], dim=0)

        confidence = {
        labels[i]: float(prediction[i])
        for i in range(len(labels))
        }

    return confidence


gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=3),
    examples=["examples/lion.jpg", "examples/cheetah.jpg"]
).launch()