import json

from src.ticket_loader import load_tickets
from src.embedding_service import EmbeddingService
from src.similarity_engine import SimilarityEngine


def evaluate():

    tickets = load_tickets(
        "data/tickets.json"
    )

    with open(
        "data/evaluation_dataset.json",
        "r",
        encoding="utf-8"
    ) as f:

        test_cases = json.load(f)

    embedding = EmbeddingService()

    engine = SimilarityEngine(
        embedding
    )

    engine.build_index(
        tickets
    )

    correct = 0

    total = len(test_cases)

    for test in test_cases:

        result = engine.search(
            test["query"],
            top_k=1
        )

        predicted = result[0]["ticket_id"]

        if predicted == test["expected_ticket_id"]:
            correct += 1

    accuracy = correct / total

    print(
        f"Accuracy: {accuracy:.2%}"
    )

    return accuracy


if __name__ == "__main__":
    evaluate()