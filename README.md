# Support Ticket Similarity Assistant

A semantic search application that helps support agents quickly find historical tickets and resolutions related to new support requests.

---

## Features

- Semantic ticket similarity search
- Top 5 relevant ticket retrieval
- Resolution recommendations
- Confidence scoring
- Streamlit UI

---

## Installation

```bash
git clone <repo>
cd support-ticket-similarity-assistant

pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Example Query

Customer cannot log into dashboard after password reset.

Output:

- Related authentication issues
- Previous resolutions
- Similarity scores

---

## Limitations

- Single-node implementation
- In-memory vector storage
- No authentication
- No ticket feedback loop

---

## Future Roadmap

- FAISS indexing
- Pinecone/Qdrant integration
- LLM-assisted summarization
- Auto-generated resolution suggestions