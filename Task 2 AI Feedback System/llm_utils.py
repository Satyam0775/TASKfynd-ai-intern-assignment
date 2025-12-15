from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

MODEL_NAME = "mistralai/mistral-7b-instruct"


# ===============================
# USER-FACING AI RESPONSE
# ===============================
def generate_user_response(review, rating):
    prompt = f"""
You are a polite and empathetic customer support assistant.

User rating: {rating}
User review: "{review}"

Write a short, friendly response to the user.
Keep it under 3 sentences.
Do not mention internal actions.
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    return response.choices[0].message.content.strip()


# ===============================
# ADMIN SUMMARY
# ===============================
def summarize_review(review, rating):
    prompt = f"""
You are an internal analytics assistant.

Summarize the following customer feedback in one short, neutral sentence.

Rating: {rating}
Review: "{review}"
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()


# ===============================
# ADMIN RECOMMENDED ACTIONS (FIXED)
# ===============================
def recommend_actions(review, rating):
    prompt = f"""
You are a customer experience analyst.

Based on the feedback below, suggest 1–2 clear business actions.

Rating: {rating}
Review: "{review}"

Return the actions as bullet points.
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    text = response.choices[0].message.content.strip()

    actions = []
    for line in text.split("\n"):
        clean = (
            line.replace("<s>", "")
                .replace("</s>", "")
                .replace("•", "")
                .strip()
        )
        if clean and len(clean) > 5:
            actions.append(clean.strip("- ").strip())

    return actions
