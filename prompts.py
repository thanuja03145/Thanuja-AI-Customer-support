
from langchain.prompts import PromptTemplate

INTENT_PROMPT = PromptTemplate(
    input_variables=["user_query"],
    template="""
You are an intent classification engine for a customer support system.
Categorize the following customer query into EXACTLY ONE of these categories:
- Product Inquiry
- Order Status
- Returns & Refunds
- Technical Support
- General Query

Customer Query: "{user_query}"

Respond with ONLY the exact category name and nothing else.
"""
)

RESPONSE_PROMPT = PromptTemplate(
    input_variables=["intent", "context", "user_query"],
    template="""
You are a helpful AI Customer Support Assistant.

Intent: {intent}
Context Information: {context}
Customer Query: {user_query}

Provide a polite, clear, and relevant response using the context information provided above.
"""
)
