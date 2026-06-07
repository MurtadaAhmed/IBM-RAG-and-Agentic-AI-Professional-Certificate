# Gradio Demos

This folder contains three Python scripts that demonstrate how to use the Gradio library to create simple web interfaces for machine learning models.

## `image_classification.py`

This script creates a web interface that can classify images. You can upload an image, and the application will tell you what it thinks is in the image, along with a confidence score.

It uses a pre-trained ResNet-18 model from PyTorch Hub to perform the classification.

### How to run

```bash
python image_classification.py
```

## `image_captioning.py`

This script creates a web interface that can generate captions for images. You can upload an image, and the application will generate a descriptive caption for it.

It uses the "BLIP" model from Hugging Face Transformers to generate the captions.

### How to run

```bash
python image_captioning.py
```

## `Introduction to Gradio.py`

This is a very simple "Hello, World!" style script that shows the basics of Gradio. It creates a web interface with a text input and a slider, and it will greet you with more or less enthusiasm depending on the slider's value.

### How to run

```bash
python "Introduction to Gradio.py"
```
