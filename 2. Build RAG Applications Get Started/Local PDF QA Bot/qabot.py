import gradio as gr
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import ChatOllama
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(
    model= "glm-4.6:cloud",
    temperature= 0.5
)

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def process_pdf_and_answer(pdf_file, user_query):
    if not pdf_file:
        return "please upload a pdf file first"
    if not user_query:
        return "please enter a question"

    print(f"Processing the document{pdf_file.name}")
    loader = PyPDFLoader(pdf_file.name)
    document = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=50
    )

    chunks = text_splitter.split_documents(document)

    print("Chunks created successfuly.")

    print("Building vector database")
    vectordb = Chroma.from_documents(chunks, embedding_model)
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    print("vector database built successfully")

    system_prompt = (
        "You are an intelligent assistant. Use the following pieces of retrieved context from a PDF "
        "to answer the question. If you don't know the answer, just say that you don't know.\n\n"
        "Context: {context}"
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}")
    ])

    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    print(f"Thinking about {user_query} ...")

    try:
        response = rag_chain.invoke({"input": user_query})
        return response['answer']
    except Exception as e:
        return f"Error analyzing document: {str(e)}"


demo = gr.Interface(
    fn=process_pdf_and_answer,
    inputs=[
        gr.File(label="Upload PDF file", file_types=['.pdf']),
        gr.Textbox(label='Input Query', lines=2, placeholder="What is this document about?")
    ],
    outputs=gr.Textbox(label="AI Analysis"),
    title="Local PDF RAG Chatbot",
    description="Upload any PDF and ask questions about it.",
)

if __name__ == "__main__":
    demo.launch()

