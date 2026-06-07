# Gradio Interface Models Documentation

This folder contains three simple Python scripts that show you how to build web interfaces for different types of applications using Gradio.

## 1. `gradio_demo.py`
**What it does:**
This is a basic calculator app that simply adds two numbers together.

**How it works:**
It creates a web page with two input boxes where you can type in numbers. When you enter the numbers, the app calculates the sum and displays the result on the screen. It is a great starting point to understand how inputs and outputs work in Gradio.

## 2. `gradio_llm.py`
**What it does:**
This app provides a straightforward question-and-answer web page powered by a local AI language model.

**How it works:**
You type a question or prompt into a text box, and the AI reads it and generates a single response. It treats every question as a brand new interaction, meaning it doesn't remember what you asked it previously.

## 3. `gradio_chatbot.py`
**What it does:**
This app creates a conversational AI chat window (similar to ChatGPT) where you can chat back and forth with an AI assistant.

**How it works:**
It uses the same underlying AI as the `gradio_llm.py` app, but it is designed specifically for conversations. As you chat, the app remembers the history of your messages, allowing you to ask follow-up questions and have a continuous, context-aware discussion.

### How to run the apps
To try any of these out, simply run them with Python in your terminal (for example: `python gradio_demo.py`). Once running, they will provide a local web address (like `http://127.0.0.1:7860`) that you can open in your web browser!