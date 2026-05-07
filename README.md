# 🏫 Campus Rules RAG Chatbot

A **Retrieval-Augmented Generation (RAG)** chatbot that answers student questions about campus rules and policies — powered by **LLaMA 3 (via Groq)**, **ChromaDB**, and **LangChain**, with a built-in **Evaluation Framework**.

---

## 🚀 Features

- 🔍 **RAG Pipeline** — Retrieves relevant rules from a vector database before answering
- 🤖 **LLaMA 3.3 70B** — Uses Groq's fast inference API for responses
- 📊 **Evaluation Framework** — Every answer is automatically scored for:
  - **Faithfulness** — Is the answer grounded in the retrieved rules?
  - **Relevance** — Were the right rules fetched?
  - **Confidence** — How clearly is the answer stated?
  - **Hallucination Detection** — Did the model make anything up?
- 💬 **Gradio UI** — Clean chat interface accessible in the browser

---

## 🗂️ Project Structure

```
campus-rules-chatbot/
├── documents/
│   └── campus_rules.txt      # Your campus rules document
├── ingest.py                 # Loads rules and builds ChromaDB
├── chatbot.py                # RAG logic + evaluation framework
├── app.py                    # Gradio chat interface
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Usage

### 1. Clone the repository
```bash
git clone https://github.com/your-username/campus-rules-chatbot.git
cd campus-rules-chatbot
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your Groq API key

create .env file and paste your grop api key there
```
> Get a free API key at [console.groq.com](https://console.groq.com)

### 5. Add your campus rules

Place your rules as plain text in:
```
documents/campus_rules.txt
```

### 6. Build the vector database
```bash
python ingest.py
```

### 7. Launch the chatbot
```bash
python app.py
```
Open your browser at **http://localhost:7860**

---

## 🧠 How It Works

```
Student Question
      │
      ▼
ChromaDB (similarity search)
      │
      ▼
Top 3 relevant rule chunks
      │
      ▼
LLaMA 3 (Groq) generates answer
      │
      ▼
LLaMA 3 evaluates its own answer
      │
      ▼
Chat UI shows answer + score card
```

---

## 📦 Tech Stack

| Tool | Purpose |
|------|---------|
| LangChain | RAG pipeline orchestration |
| ChromaDB | Vector database |
| SentenceTransformers (`all-MiniLM-L6-v2`) | Text embeddings |
| Groq + LLaMA 3.3 70B | LLM for answers & evaluation |
| Gradio | Chat UI |

---

## ⚠️ Important Notes

- The `campus_db/` folder is excluded from Git (listed in `.gitignore`) — run `ingest.py` locally to rebuild it
- Never commit your Groq API key — consider using a `.env` file with `python-dotenv` for production
- `venv/` is also excluded — use `requirements.txt` to recreate it

---

## 🙌 Acknowledgements

Built as a learning project to explore RAG pipelines, vector search, and LLM evaluation.
