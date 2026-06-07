# Local RAG Lab Documentation

This lab (`local_rag_lab`) demonstrates how to build a simple Retrieval Augmented Generation (RAG) application using LangChain. It allows you to chat with a private HR assistant that answers questions based on a company policy document.

## `step1_indexing.py` Script Breakdown:

Here's a breakdown of what the `step1_indexing.py` script does:

1.  **Download Company Policies**: It first downloads a text file named `companyPolicies.txt` from a URL if it doesn't already exist locally. This file contains the information the HR assistant will use.

2.  **Load and Split Document**: The `companyPolicies.txt` file is loaded and then split into smaller, manageable chunks of text. This helps the RAG system process information more efficiently.

3.  **Create Embeddings**: Each text chunk is converted into a numerical representation called an "embedding" using a pre-trained HuggingFace model (`sentence-transformers/all-MiniLM-L6-v2`). Embeddings capture the semantic meaning of the text.

4.  **Set up Vector Store and Retriever**: These embeddings are stored in a `Chroma` vector store. A "retriever" is then created from this vector store. When you ask a question, the retriever will find the most relevant text chunks from the `companyPolicies.txt` based on your question's embedding.

5.  **Initialize Large Language Model (LLM)**: A local Large Language Model (LLM) is initialized using `ChatOllama` with the `glm-4.6:cloud` model. This LLM will generate the answers.

6.  **Create RAG Chain**: The script sets up a RAG chain. This chain combines the retriever (to find relevant information) and the LLM (to generate an answer based on that information). It also includes a system prompt to guide the LLM's responses, telling it to use the provided context and to be concise and professional.

7.  **Interactive Chat**: Finally, the script starts an interactive loop where you can type questions. The RAG chain processes your question, retrieves relevant policy information, and the LLM generates an answer. You can type 'quit', 'exit', or 'bye' to stop the chat.

## How to Run the Lab:

1.  **Install Dependencies**: Make sure you have all the necessary Python libraries installed. You can typically install them using pip:
    ```bash
    pip install langchain langchain-community langchain-huggingface langchain-chroma langchain-ollama langchain-classic langchain-core
    ```
2.  **Start Ollama and Pull Model**: Ensure you have Ollama running and the `glm-4.6:cloud` model pulled. If not, you can do so with:
    ```bash
    ollama run glm-4.6:cloud
    ```
    (You might need to install Ollama first if you haven't already.)
3.  **Run the Script**: Navigate to the `local_rag_lab` directory in your terminal and run the Python script:
    ```bash
    python step1_indexing.py
    ```
4.  **Start Chatting**: You will then be prompted to ask questions to your private HR assistant. Type your questions and press Enter. To exit, type `quit`, `exit`, or `bye`.
