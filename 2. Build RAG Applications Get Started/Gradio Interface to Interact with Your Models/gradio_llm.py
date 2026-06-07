import gradio as gr
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

llm = ChatOllama(
    model= "glm-4.6:cloud",
    temperature=0.7
)

def ask_local_ai(user_prompt):
    if not user_prompt.strip():
        return "please enter a question"
    try:
        response = llm.invoke([HumanMessage(content=user_prompt)])
        return response.content
    except Exception as e:
        return f"Error connection to Ollama: {str(e)}"

demo = gr.Interface(
    fn=ask_local_ai,
    inputs=gr.Textbox(lines=3, placeholder="As anything...", label="Your question"),
    outputs=gr.Textbox(label="AI response"),
    title="Local LLM playground",
    description="Powered by Ollama and Gradio"
)

if __name__ == "__main__":
    demo.launch()