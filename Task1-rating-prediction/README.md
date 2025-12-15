# Fynd AI Intern – Take Home Assessment

This repository contains the complete submission for the **Fynd AI Intern – Take Home Assessment**, covering both **Task 1 (Prompt Engineering)** and **Task 2 (Two-Dashboard AI Feedback System)**.

---

## 🔹 Task 1: Rating Prediction via Prompt Engineering

### Overview
This task focuses on using **prompt engineering techniques** to classify Yelp reviews into star ratings (1–5) using a **Large Language Model (LLM)**.  
No machine learning model was trained; the task evaluates how different prompt designs influence LLM output quality.

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
Zero-shot prompting
Few-shot prompting
Structured prompting with strict output constraints

Evaluation
Prompt versions were compared based on:
Accuracy (actual vs predicted stars)

JSON validity rate
Output consistency
A smaller sample size was used due to free-tier API limits.
Repository Structure (Task 1)
notebooks/
prompts/
data/
outputs/

Conclusion
Structured prompting produced the most reliable and consistent results across all evaluation metrics.

## 🔹 Task 2: Two-Dashboard AI Feedback System (Web-Based)
Overview
Task 2 involves building and deploying a web-based AI feedback system with two dashboards:

User Dashboard (Public-Facing)
Admin Dashboard (Internal-Facing)
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
User rating
User review
AI-generated summary
AI-suggested recommended actions
Additional analytics include:
Total number of reviews
Average rating

🤖 LLM Usage in Task 2
LLMs are used for:
User-facing response generation
Review summarisation
Recommended next actions for admins

🛠 Tech Stack
Python
Streamlit
OpenRouter (Mistral-7B-Instruct)
JSON (lightweight shared storage)
Hugging Face Spaces

👤 Author
Satyam Kumar
