from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from config import MODEL_ID, TEMPERATURE

class AIResponse(BaseModel):
    summary: str = Field(description="Summary of the user's message")
    sentiment: int = Field(description="Sentiment score from 0 (negative) to 100 (positive)")
    response: str = Field(description="Suggested response to the user")
    next_step: str = Field(description="Recommended next action for the customer support rep to take")

json_parser = JsonOutputParser(pydantic_object=AIResponse)

llm = ChatOllama(
    model=MODEL_ID,
    temperature=TEMPERATURE
)

template = """
System: {system_prompt}
{format_prompt}
Human: {user_prompt}
AI:
"""

prompt_template = PromptTemplate(
    template=template,
    input_variables=["system_prompt", "format_prompt", "user_prompt"]
)

def get_ai_response(system_prompt, user_prompt):
    chain = prompt_template | llm | json_parser

    return chain.invoke({
        'system_prompt': system_prompt,
        'user_prompt': user_prompt,
        'format_prompt': json_parser.get_format_instructions()
    })

