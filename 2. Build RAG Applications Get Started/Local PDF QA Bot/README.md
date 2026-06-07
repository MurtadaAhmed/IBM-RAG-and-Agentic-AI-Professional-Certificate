# Local PDF QA Bot Documentation

This folder contains `qabot.py`, a script that creates a local web application where you can upload a PDF document and ask questions about its contents. 

## `qabot.py`

**What it does:**
This app acts as a smart reading assistant. You upload a PDF document (like a manual, an article, or a report) and type a question. The AI will read through the document, find the specific sections that contain the answer, and write out a clear response based *only* on the document you provided.

**How it works:**
This script uses a technique called **RAG** (Retrieval-Augmented Generation). Here is the step-by-step breakdown of what happens under the hood when you hit "Submit":

1. **Loading:** The app reads your uploaded PDF file and extracts all of its text.
2. **Splitting:** Since AI models can't read an entire book at once, the app chops the document up into smaller, overlapping chunks of text (about 1000 characters each).
3. **Embedding & Storing:** It uses a mathematical model (from Hugging Face) to convert these text chunks into numbers (vectors) and stores them in a temporary, searchable database called Chroma.
4. **Retrieval:** When you ask a question, the app turns your question into numbers too. It then searches the database to find the top 3 chunks of text from the PDF that are most similar to your question.
5. **Answering:** Finally, the app hands those 3 relevant text chunks and your original question over to the local AI language model (Ollama). It tells the AI: *"Use ONLY this provided text to answer the user's question."* The AI then generates and displays the final answer.

### Key Technologies Used
* **Gradio:** Builds the web interface (file uploader and text boxes).
* **LangChain:** The framework that wires all the different AI steps (loading, splitting, retrieving, and prompting) together.
* **Chroma:** The vector database used to store the text chunks.
* **Hugging Face:** Provides the embedding model to translate text into search-friendly vectors.
* **Ollama:** Powers the main AI language model that reads the retrieved context and talks to you.

### How to run the app
To try it out, open your terminal, navigate to this folder, and run:
```bash
python qabot.py
```
Once it is running, it will provide a local web address (usually `http://127.0.0.1:7860`). Open that link in your web browser, upload a PDF, and start asking questions!