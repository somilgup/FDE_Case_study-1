import streamlit as st

from src.ticket_loader import load_tickets
from src.embedding_service import EmbeddingService
from src.similarity_engine import SimilarityEngine
from src.utils import clean_text


st.set_page_config(
    page_title="Support Ticket Similarity Assistant",
    layout="wide"
)

st.title("Support Ticket Similarity Assistant")

st.write(
    "Enter a new support ticket and discover similar historical tickets along with their resolutions."
)

tickets = load_tickets(
    "data/tickets.json"
)

embedding_service = EmbeddingService()

engine = SimilarityEngine(
    embedding_service
)

engine.build_index(
    tickets
)

ticket_text = st.text_area(
    "Enter a new support ticket",
    height=200,
    placeholder="Example: Customer cannot log in after resetting password. Login page says password is incorrect."
)

if st.button("Find Similar Tickets"):

    if not ticket_text.strip():

        st.warning(
            "Please enter a ticket description."
        )

    else:

        cleaned_ticket = clean_text(
            ticket_text
        )

        results = engine.search(
            cleaned_ticket,
            top_k=5
        )

        st.subheader("Top Similar Tickets")

        for r in results:

            confidence = round(
                r["score"] * 100,
                2
            )

            with st.expander(
                f"{r['subject']} ({confidence}%)"
            ):

                st.write(
                    f"**Ticket ID:** {r['ticket_id']}"
                )

                st.write(
                    f"**Category:** {r['category']}"
                )

                st.write(
                    f"**Original Issue:**"
                )

                st.write(
                    r["description"]
                )

                st.write(
                    f"**Resolution:**"
                )

                st.write(
                    r["resolution_notes"]
                )

                st.progress(
                    float(r["score"])
                )

                st.caption(
                    f"Similarity Score: {confidence}%"
                )