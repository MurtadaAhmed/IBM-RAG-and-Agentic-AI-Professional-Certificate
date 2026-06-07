import gradio as gr
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage

llm = ChatOllama(
    model="glm-4.6:cloud",
    temperature=0.5
)

def chat_with_ai(message, history):
    langchain_messages = []

    for item in history:
        if isinstance(item, dict):
            if item.get("role") == "user":
                langchain_messages.append(HumanMessage(content=item.get("content", "")))
            elif item.get("role") == "assistant":
                langchain_messages.append(AIMessage(content=item.get("content", "")))

    langchain_messages.append(HumanMessage(content=message))
    print(f"User sent: {message} | History items: {len(history)}")

    try:
        response = llm.invoke(langchain_messages)
        return response.content
    except Exception as e:
        return f"Error connection to Ollama: {str(e)}"

demo = gr.ChatInterface(
    fn=chat_with_ai,
    title="Local Support Chat",
    description="Ask a question",
    examples=["Hello!", "What can you help me with?", "Tell me a short joke."]
)

if __name__ == "__main__":
    demo.launch()