# Fynd AI Intern – Take Home Assessment  

This repository contains the complete submission for the **Fynd AI Intern Take Home Assessment**, covering both **Task 1 (Prompt Engineering)** and **Task 2 (Two-Dashboard AI Feedback System)**.

---

## 🔹 Task 1: Rating Prediction via Prompt Engineering

### Overview
This task focuses on using **prompt engineering techniques** to classify Yelp reviews into star ratings (1–5) using a **Large Language Model (LLM)**, without training any machine learning model.

### Dataset
- Yelp Reviews Dataset sourced from Kaggle  
- A cleaned and randomly sampled subset was used for evaluation

### LLM Used
- **Provider:** OpenRouter  
- **Model:** `mistralai/mistral-7b-instruct`

### Output Format
```json
{
  "predicted_stars": 4,
  "explanation": "Brief reasoning for the assigned rating."
}
Prompting Approaches
Zero-Shot Prompt
Few-Shot Prompt
Structured Prompt

Evaluation
Prompt versions were compared based on:
Accuracy (actual vs predicted stars)
JSON validity
Output consistency
A smaller sample size was used due to free-tier API limits.

Repository Structure (Task 1)
notebooks/
prompts/
data/
outputs/

Conclusion
Structured prompting produced the most reliable and consistent results.

🔹 Task 2: Two-Dashboard AI Feedback System (Web-Based)
Overview
Task 2 involves building and deploying a web-based AI feedback system with two dashboards:

A User Dashboard (public-facing)

An Admin Dashboard (internal-facing)

Both dashboards read and write from a shared data source and use an LLM for generating responses, summaries, and recommended actions.

🧑‍💻 User Dashboard (Public-Facing)
Users can:

Select a star rating (1–5)
Write a short review
Submit feedback
On submission:
An AI-generated response is shown to the user
Feedback is stored in a shared JSON-based data store

🧑‍💼 Admin Dashboard (Internal-Facing)
Admins can view a live-updating list of all submissions, including:
User r
User review
AI-generated summary
AI-suggested recommended actions
Additional analytics:
Total number of reviews
Average rating

🤖 LLM Usage in Task 2
LLMs are used for:

User-facing response generation

Review summarisation

Recommended next actions for admins

🌐 Deployment
The application is deployed using Hugging Face Spaces (Streamlit).

🔗 Live Application (User & Admin Dashboards):
https://huggingface.co/spaces/Satyam0077/ai-feedback-system-fynd

Both dashboards are accessible via the same URL using a dashboard selector.
Repository Structure (Task 2)
pgsql
Copy code

🛠 Tech Stack
Python
Streamlit
OpenRouter (Mistral-7B-Instruct)
JSON (lightweight shared storage)
Hugging Face Spaces

👤 Author
Satyam Kumar
