import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from intent_classifier import classify_intent
from knowledge_base import get_knowledge_response
from prompts import RESPONSE_PROMPT

load_dotenv()

def main():
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("❌ Error: GEMINI_API_KEY not found in .env file.")
        return

    try:
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key, temperature=0.7)
    except Exception as e:
        print(f"❌ Error: {e}")
        return

    print("==================================================")
    print("🤖 Welcome to AI Customer Support Assistant!")
    print("Type 'exit' or 'quit' to end the conversation.")
    print("==================================================\n")

    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                print("Bot: Please enter a valid query.\n")
                continue

            if user_input.lower() in ["exit", "quit"]:
                print("Bot: Thank you! Have a great day! 👋")
                break

            intent = classify_intent(user_input)
            context = get_knowledge_response(intent)
            formatted_prompt = RESPONSE_PROMPT.format(intent=intent, context=context, user_query=user_input)
            response = llm.invoke(formatted_prompt)

            print(f"\n[Detected Intent: {intent}]")
            print(f"Bot: {response.content}\n")

        except Exception as e:
            print(f"❌ Error: {e}\n")

if __name__ == "__main__":
    main()


