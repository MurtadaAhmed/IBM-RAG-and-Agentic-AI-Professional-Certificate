from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

model = ChatOllama(
    model="glm-4.6:cloud",
    temperature=0.0
)

text = "Only reply with the answer. What is the capital of Canada?"

response = model.invoke([HumanMessage(content=text)])

print(response.content)