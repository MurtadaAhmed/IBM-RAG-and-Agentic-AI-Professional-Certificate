from llama_index.core import Settings, Document, VectorStoreIndex, PromptTemplate
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from mock_data import get_formatted_profile

print("loading embedding model")
Settings.embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("loading ollama model")
Settings.llm = Ollama(
    model="glm-4.6:cloud",
    request_timeout=120.0,
    temperature=0.7
)

print("formatting profile data")
profile_text = get_formatted_profile()

documents = [Document(text=profile_text)]

print("building the vector index")

index = VectorStoreIndex.from_documents(documents)

print("LlamaIndex setup is complete")

print("configuring the ai prompt")

prompt_template_str = (
"You are an expert professional networker and recruiter. "
    "Below is the professional profile of a candidate:\n"
    "---------------------\n"
    "{context_str}\n"
    "---------------------\n"
    "Based ONLY on this profile, write a short, engaging, and highly personalized LinkedIn connection request message (under 300 characters). "
    "Mention a specific detail from their experience or interests to break the ice. "
    "Do not hallucinate any details not present in the profile.\n\n"
    "Icebreaker Message:"
)

icebreaker_prompt = PromptTemplate(prompt_template_str)

print("generating personalized icebreaker")

query_engine = index.as_query_engine(
    text_qa_template=icebreaker_prompt
)

response = query_engine.query("Draft the LinkedIn message")

print(response)