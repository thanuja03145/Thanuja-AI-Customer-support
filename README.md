# Thanuja-AI-Customer-support
# AI Customer Support Assistant

An AI-powered Customer Support Assistant built with **Python**, **LangChain**, and **Google Gemini API** 

## 📌 Features

* **Conversational Interface:** Interactive CLI-based chat flow until the user exits.
* **Intent Classification:** Dynamically classifies queries into *Product Inquiry*, *Order Status*, *Returns & Refunds*, *Technical Support*, or *General Query*.
* **Knowledge Retrieval:** Retrieves predefined grounding responses based on detected intent.
* **LLM Response Generation:** Generates clear, helpful responses powered by Gemini LLM.
* **Graceful Error Handling:** Handles empty input, missing API keys, and connection errors smoothly.
* **Secure Key Storage:** Uses `.env` for managing API credentials safely.

---
## Demo & screenshots

![Application Demo](demo.png)

---

## 📂 Project Structure
AI-Customer-Support-Assistant/
├── chat.py # Main application entry point
├── intent_classifier.py # Intent classification logic using LLM
├── knowledge_base.py # Predefined knowledge base & retrieval logic
├── prompts.py # Prompt templates for Intent & Response generation
├── requirements.txt # Required dependencies
├── .env.example # Environment template file
├── .gitignore # Files to ignore in Git repository
└── README.md # Project documentation

---

## 🛠️ Dependencies & Technologies

* **Python 3.10+**
* **LangChain**
* **LangChain Google GenAI (`gemini-2.5-flash`)**
* **python-dotenv**

---

## 🚀 Installation & Setup

### 1. Clone the repository
git clone <your-github-repo-link>
cd <your-repo-folder>

### 2. Install required packages
pip install -r requirements.txt
python chat.py

### 3. Setup API Key
Create a `.env` file in the project root:
GEMINI_API_KEY=your_actual_gemini_api_key_here

### 4. Run the Application
python chat.py

