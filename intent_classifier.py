mport os
from langchain_google_genai import ChatGoogleGenerativeAI
from prompts import INTENT_PROMPT

def classify_intent(user_query: str) -> str:
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            return "General Query"
            
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key, temperature=0)
        formatted_prompt = INTENT_PROMPT.format(user_query=user_query)
        response = llm.invoke(formatted_prompt)
        
        intent = response.content.strip()
        valid_intents = ["Product Inquiry", "Order Status", "Returns & Refunds", "Technical Support", "General Query"]
        
        if intent in valid_intents:
            return intent
        return "General Query"
    except Exception:
        return "General Query"
