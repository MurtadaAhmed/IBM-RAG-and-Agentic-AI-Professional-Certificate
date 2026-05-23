from model import get_ai_response

system_instructions = "You are an AI assistant helping with customer inquiries. Provide a helpful and concise response."
user_question = "I ordered a laptop two weeks ago and it still hasn't arrived. The tracking number is completely broken and I am very frustrated!"

result = get_ai_response(system_instructions, user_question)

print("--- AI JSON Data ---")
print(f"summary: {result['summary']}")
print(f"Sentiment Score: {result['sentiment']}/100")
print(f"Response: {result['response']}")
print(f"Rep Next Step: {result['next_step']}")