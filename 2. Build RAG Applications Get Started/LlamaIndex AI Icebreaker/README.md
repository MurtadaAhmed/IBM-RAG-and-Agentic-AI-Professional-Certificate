# AI Icebreaker Bot Documentation

This folder contains `icebreaker_bot.py`, a Python script that reads a professional profile and automatically writes a personalized LinkedIn connection request.

## What it does
Imagine you want to connect with someone on LinkedIn, but you don't know what to say. This bot acts as your personal networking assistant. It reads a person's professional background, experience, and interests, and then crafts a short, engaging message (under 300 characters) designed to "break the ice" and start a conversation.

## How it works
Here is a step-by-step breakdown of what happens when you run the script:

1. **Preparing the AI:** The script first loads two AI models. One model (from Hugging Face) is used to read and understand the text, and the other (Ollama) is the language model used to write the final message.
2. **Reading the Profile:** It grabs a mock professional profile (from the `mock_data.py` file) and turns it into a text document that the AI can read.
3. **Organizing the Data:** It stores the profile information in a searchable format called a "Vector Index" so the AI can quickly find relevant details. 
4. **Setting the Rules:** The script gives the AI a strict set of instructions (a "prompt"). It tells the AI to act like a professional networker, keep the message short, and mention a specific detail from the person's profile to make it feel personal.
5. **Writing the Message:** Finally, it asks the AI to draft the message based on the profile data and the rules, and then prints the result on your screen.

## Key Technologies Used
* **LlamaIndex:** The main framework used to organize our data and connect it to the AI models.
* **Hugging Face:** Provides the model that helps the computer map out and understand the text.
* **Ollama:** Powers the main AI language model that actually writes the icebreaker message.

## Files in this Folder
* `icebreaker_bot.py`: The main program that runs the AI assistant.
* `mock_data.py`: A file containing a fake professional profile (Alex Morgan) used to test the bot.
* `dependencies.txt`: A list of the required Python packages needed to run the program.

## How to run the app
To try it out, open your terminal, navigate to this folder, and run:
```bash
python icebreaker_bot.py
```

Wait a few moments, and the personalized LinkedIn connection message will be printed directly in your terminal!