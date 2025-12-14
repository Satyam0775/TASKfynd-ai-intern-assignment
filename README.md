 ## Task 1: Rating Prediction via Prompt Engineering

## Overview
This repository contains the solution for Task 1 of the Fynd AI Intern Take Home Assessment. The task focuses on using prompt engineering techniques to classify Yelp reviews into star ratings (1–5) using a Large Language Model (LLM), without training any machine learning model.

## Dataset
Yelp Reviews Dataset sourced from Kaggle. A cleaned and randomly sampled subset was used for evaluation.

## LLM Used
- Provider: OpenRouter  
- Model: mistralai/mistral-7b-instruct  

## Output Format
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

Repository Structure
notebooks/
prompts/
data/
outputs/

Conclusion

Structured prompting produced the most reliable and consistent results.

Author
Satyam Kumar
