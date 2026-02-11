# LLM-Based Query Analyzer (LangChain)

This project demonstrates how to build a structured, production-style **LLM-powered query analysis system** using LangChain and OpenAI models.

The system analyzes raw user queries, identifies intent and topic, and returns **schema-validated structured outputs**, making it suitable for real-world applications such as intelligent search, chat systems, and AI-assisted workflows.

---

## 🚀 Features
- Intent and topic extraction from natural language queries
- Structured outputs using **Pydantic schemas**
- Prompt chaining with LangChain (LCEL)
- Deterministic and validated LLM responses
- Clean separation between prompt, model, and output parsing

---

## 🧠 Tech Stack
- Python
- LangChain
- OpenAI API
- Pydantic
- dotenv

---

## ⚙️ How It Works
1. User enters a natural language query
2. The query is passed through a structured LangChain pipeline
3. The LLM analyzes intent, urgency, and topic
4. Output is returned in a validated JSON schema

---

## ▶️ How to Run
```bash
pip install langchain langchain-openai python-dotenv pydantic
python main.py
