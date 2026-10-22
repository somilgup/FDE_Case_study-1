from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class SimilarityEngine:

    def __init__(self, embedding_service):
        self.embedding_service = embedding_service
        self.ticket_vectors = None
        self.tickets = None

    def build_index(self, tickets):

        self.tickets = tickets

        texts = [
            f"""
            {t.get('category', '')}
            {' '.join(t.get('tags', []))}
            {t.get('subject', '')}
            {t.get('description', '')}
            """
            for t in tickets
        ]

        self.ticket_vectors = self.embedding_service.model.encode(
            texts,
            convert_to_numpy=True
        )

    def search(self, query, top_k=5):

        query_vector = self.embedding_service.generate(query)

        scores = cosine_similarity(
            [query_vector],
            self.ticket_vectors
        )[0]

        ranked = np.argsort(scores)[::-1]

        results = []

        for idx in ranked[:top_k]:

            ticket = self.tickets[idx]

            results.append(
                {
                    "ticket_id": ticket.get("ticket_id", ""),
                    "category": ticket.get("category", ""),
                    "subject": ticket.get("subject", ""),
                    "description": ticket.get("description", ""),
                    "resolution_notes": ticket.get(
                        "resolution_notes",
                        ticket.get("resolution", "")
                    ),
                    "score": float(scores[idx])
                }
            )

        return results