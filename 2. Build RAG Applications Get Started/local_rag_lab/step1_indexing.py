import urllib.request
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from pathlib import Path
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import ChatOllama
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/6JDbUb_L3egv_eOkouY71A.txt'
filename = 'companyPolicies.txt'


file_path = Path(filename)
if not file_path.exists():
    urllib.request.urlretrieve(url, filename)

loader = TextLoader(filename)
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = Chroma.from_documents(texts, embedding_model)

retriever = vector_store.as_retriever(search_kwargs={"k": 2})
print("vector store and retriever are set up successfully")

llm = ChatOllama(
    model="glm-4.6:cloud",
    temperature=0.2
)

system_prompt = (
    "You are a helpful assistant. Use the following pieces of retrieved context to answer the question. "
    "If you don't know the answer based on the context, just say that you don't know. "
    "Keep the answer concise and professional.\n\n"
    "Context: {context}"
)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}")
])

question_answer_chain = create_stuff_documents_chain(llm, prompt)

rag_chain = create_retrieval_chain(retriever, question_answer_chain)

print("\n" + "=" * 50)
print("Welcome to your Private HR Assistant!")
print("Type 'quit', 'exit', or 'bye' to stop the chat.")
print("=" * 50 + "\n")

while True:
    query = input("\nQuestion: ")

    if query.lower() in ["quit", "exit", "bye"]:
        print("Answer: Goodbye!")
        break

    print("Thinking...")

    response = rag_chain.invoke({"input": query})

    print("\nAnswer: ")
    print(response["answer"])