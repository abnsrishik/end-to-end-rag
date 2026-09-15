# End-to-End Agentic AI Chatbot (RAG)

Agentic RAG chatbot built with **LangGraph** + **LangChain**. Retrieves from multiple sources (web, Wikipedia, Arxiv, local FAISS vector store) and answers questions via a Streamlit UI.

---

## Architecture

```
app.py
  └── src/LangGraphAgenticAI/main.py   ← Streamlit app entry point
        ├── LangGraph agent graph
        ├── Tool nodes (Tavily web search, Wikipedia, Arxiv, FAISS retriever)
        ├── Groq LLM (via langchain-groq)
        └── HuggingFace embeddings → FAISS index (AINews/ docs)
```

---

## Features

- Multi-source retrieval: web (Tavily), Wikipedia, Arxiv, local vector store (FAISS)
- Agentic loop via LangGraph — model decides which tool to call
- LLM: Groq (fast inference)
- Embeddings: HuggingFace `sentence-transformers`
- UI: Streamlit

---

## Setup

### Prerequisites

- Python 3.11+ (see `.python-version`)
- Groq API key
- Tavily API key

### Install

```bash
git clone https://github.com/abnsrishik/end-to-end-rag.git
cd end-to-end-rag

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

### Environment Variables

Create `.env` in project root:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## Run

```bash
streamlit run app.py
```

---

## Project Structure

```
end-to-end-rag/
├── AINews/                  # Source documents for FAISS vector store
├── src/
│   └── LangGraphAgenticAI/  # Core agent logic
│       └── main.py          # load_langgraph_agentic_app()
├── app.py                   # Streamlit entry point
├── main.py                  # CLI hello (dev scaffold)
├── requirements.txt
├── pyproject.toml
└── .python-version
```

---

## Dependencies

| Package | Purpose |
|---|---|
| `langgraph` | Agent graph orchestration |
| `langchain-groq` | Groq LLM integration |
| `langchain_huggingface` | HuggingFace embeddings |
| `faiss-cpu` | Local vector store |
| `langchain-tavily` | Web search tool |
| `arxiv` | Arxiv paper retrieval |
| `wikipedia` | Wikipedia tool |
| `streamlit` | Chat UI |
| `sentence-transformers` | Embedding model |

---

## License

MIT
