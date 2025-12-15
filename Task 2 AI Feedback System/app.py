import streamlit as st
from storage import load_data, save_feedback
from llm_utils import (
    generate_user_response,
    summarize_review,
    recommend_actions
)

st.set_page_config(page_title="AI Feedback System", layout="wide")

st.title("🧠 AI Feedback System")

# -------------------------------
# Dashboard Selector
# -------------------------------
view = st.selectbox(
    "Select Dashboard View",
    ["User Dashboard", "Admin Dashboard"]
)

# ===============================
# 🧑‍💻 USER DASHBOARD (PUBLIC)
# ===============================
if view == "User Dashboard":
    st.header("🧑‍💻 User Feedback")

    rating = st.selectbox("Select Rating", [1, 2, 3, 4, 5])
    review = st.text_area("Write your review")

    if st.button("Submit Review"):
        if review.strip() == "":
            st.warning("Please write a review before submitting.")
        else:
            # ---- LLM Calls ----
            ai_response = generate_user_response(review, rating)
            summary = summarize_review(review, rating)
            actions = recommend_actions(review, rating)

            # ---- Store everything in shared data ----
            entry = {
                "rating": rating,
                "review": review,
                "ai_response": ai_response,
                "ai_summary": summary,
                "recommended_actions": actions
            }

            save_feedback(entry)

            # ---- User-facing output ----
            st.success("Review submitted successfully!")
            st.subheader("AI Response")
            st.write(ai_response)

# ===============================
# 🧑‍💼 ADMIN DASHBOARD (INTERNAL)
# ===============================
elif view == "Admin Dashboard":
    st.header("🧑‍💼 Admin Dashboard")

    data = load_data()

    if not data:
        st.info("No feedback submitted yet.")
    else:
        avg_rating = round(
            sum(item["rating"] for item in data) / len(data), 2
        )

        col1, col2 = st.columns(2)
        col1.metric("Total Reviews", len(data))
        col2.metric("Average Rating", avg_rating)

        st.divider()

        for i, item in enumerate(reversed(data), start=1):
            st.subheader(f"Feedback #{i}")

            st.write(f"⭐ **Rating:** {item['rating']}")
            st.write(f"📝 **Review:** {item['review']}")

            st.write("🤖 **AI Summary:**")
            st.write(item.get("ai_summary", "Not available"))

            st.write("📌 **Recommended Actions:**")
            actions = item.get("recommended_actions", [])
            if actions:
                for act in actions:
                    st.write(f"- {act}")
            else:
                st.write("No actions available")

            st.divider()
