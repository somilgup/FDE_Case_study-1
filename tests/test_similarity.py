from src.embedding_service import EmbeddingService
from src.similarity_engine import SimilarityEngine


def test_similarity_returns_results():

    tickets = [
        {
            "ticket_id": 1,
            "subject": "Login issue",
            "description": "Cannot login",
            "resolution": "Reset password"
        }
    ]

    embedding = EmbeddingService()

    engine = SimilarityEngine(
        embedding
    )

    engine.build_index(
        tickets
    )

    results = engine.search(
        "Unable to login"
    )

    assert len(results) == 1

    assert results[0]["ticket_id"] == 1


def test_scores_present():

    tickets = [
        {
            "ticket_id": 1,
            "subject": "API timeout",
            "description": "Request timeout",
            "resolution": "Increase timeout"
        }
    ]

    embedding = EmbeddingService()

    engine = SimilarityEngine(
        embedding
    )

    engine.build_index(
        tickets
    )

    results = engine.search(
        "API timeout problem"
    )

    assert "score" in results[0]