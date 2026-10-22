from sentence_transformers import SentenceTransformer


class EmbeddingService:

    def __init__(self):
        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

    def generate(self, text):
        return self.model.encode(
            text,
            convert_to_numpy=True
        )
