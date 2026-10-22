# Support Ticket Similarity Assistant

## Problem Statement

Support agents frequently receive issues that are similar to previously resolved tickets. Without visibility into historical resolutions, agents spend additional time investigating known issues and may provide inconsistent answers.

The goal is to provide agents with historical tickets that are semantically similar to a new incoming ticket along with resolution information.

---

## Assumptions

- Current volume is 150 tickets/day.
- Historical dataset may grow to 100k+ tickets.
- Agent response time should be under one second.
- Ticket data includes subject, description and resolution.

---

## Architecture

Historical Tickets
      |
      V
Embedding Generation
      |
      V
Vector Index
      |
      |
New Ticket
      |
Embedding
      |
Similarity Search
      |
Top Matches

---

## Approach

The solution uses Sentence Transformers to generate semantic embeddings from ticket content.

Each historical ticket is converted into a vector representation.

When a new ticket arrives:

1. Generate embedding
2. Compute cosine similarity
3. Retrieve top matching tickets
4. Display historical resolutions

---

## Tradeoffs Considered

### TF-IDF

Pros:
- Simple
- Fast

Cons:
- Keyword dependent
- Poor semantic understanding

### Embeddings (Chosen)

Pros:
- Semantic understanding
- Better scalability
- Improved relevance

Cons:
- Higher compute cost

---

## Future Improvements

- Hybrid Search (BM25 + Vector Search)
- Vector Database (Pinecone/Qdrant)
- LLM Resolution Summaries
- Auto Response Recommendation
- Agent Feedback Loop