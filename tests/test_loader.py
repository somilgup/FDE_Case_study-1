from src.ticket_loader import load_tickets


def test_load_tickets():

    tickets = load_tickets(
        "data/tickets.json"
    )

    assert len(tickets) > 0

    assert "subject" in tickets[0]

    assert "resolution" in tickets[0]