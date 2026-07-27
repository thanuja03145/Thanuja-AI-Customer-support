AI CUSTOMER SUPPORT ASSISTANT
## 👤 Developer Information
* **Project Title:** ThanujaK-AI-Customer-Support
* **Developer Name:** Thanuja K

---
##📸Aplication Demo

![chatbot screenshot](100006730.jpg)
![chatbot screenshot](100006731.png)

---

## 💡 Key Features

* **Interactive CLI Interface:** Continuous conversation loop running smoothly until user exits (`exit`/`quit`).
* **Automated Intent Classification:** Categorizes user input dynamically into *Product Inquiry*, *Order Status*, *Returns & Refunds*, *Technical Support*, or *General Query*.
* **Grounded Knowledge Retrieval:** Fetches precise internal policy facts based on the detected intent.
* **LLM Response Generation:** Employs LangChain with Google Gemini API (`gemini-2.5-flash`) for smart answers.
* **Resilient Error Handling:** Smoothly manages invalid API keys, connection issues, and empty prompt inputs.
* **Environment Security:** Uses `.env` configuration to protect private API keys.

---

## 🛠️ Troubleshooting Tips

| Problem | Likely Cause | Solution |
| :--- | :--- | :--- |
| `ModuleNotFoundError: No module named 'langchain'` | Dependencies not installed | Run `pip install -r requirements.txt` |
| Bot always returns default query error | Invalid/Missing `GEMINI_API_KEY` | Verify key inside `.env` file |
| `[API Error]: 401 ...` in terminal | Expired or wrong API key | Update your Gemini API key in `.env` |
| `python` not recognized (Windows) | Python not added to PATH | Reinstall Python and check "Add to PATH" |
| `running scripts is disabled` | PowerShell security setting | Run `Set-ExecutionPolicy -Scope Process RemoteSigned` |
| `.env` values not loading | File misnamed or misplaced | Ensure file is named strictly `.env` in root folder |

---

## 🧩 How the Files Work Together

1. **User opens terminal/CLI** -> Launches `chat.py`.
2. **User types a query** -> `chat.py` sends input to `intent_classifier.py`.
3. **`intent_classifier.py` categorizes intent** -> Uses Gemini API to detect intent.
4. **`knowledge_base.py` pulls context** -> Fetches matching knowledge response.
5. **`prompts.py` formats input** -> Combines intent, context, and user message into a structured template.
6. **Gemini LLM processes request** -> Returns polite final response.
7. **Terminal renders reply** -> Displays category tag and formatted text to user.

---

## 📚 Tech Stack Summary

* **Backend:** Python 3.10+
* **LLM Orchestration:** LangChain
* **AI Model:** Google Gemini (`gemini-2.5-flash`)
* **Config Management:** `python-dotenv`

---

## 📂 Project Directory Structure

ThanujaK-AI-Customer-Support/
├── screenshots/ # Directory containing all 14 demo screenshots
│ ├── image1.png
│ ├── image2.png
│ ├── ...
│ └── image14.png
├── chat.py # Core application entry point
├── intent_classifier.py # Intent categorization engine
├── knowledge_base.py # Knowledge store & retrieval logic
├── prompts.py # Prompt templates
├── requirements.txt # Package dependencies
├── .env.example # Environment variable template
├── .gitignore # Git ignore rules
└── README.md # Complete project documentation

---

## ⚙️ Installation & Usage Guide

### 1. Clone repository
git clone <your-github-repository-url>
cd ThanujaK-AI-Customer-Support

### 2. Install dependencies
pip install -r requirements.txt

### 3. Configure `.env`
GEMINI_API_KEY=your_actual_gemini_api_key_here

### 4. Run application
python chat.py

