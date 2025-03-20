# News Summarization and Text-to-Speech Application

This repository contains a complete project for analyzing news articles about companies using Natural Language Processing (NLP) techniques. The project includes both frontend and backend components, as well as multiple data processing steps.

## Overview

The project consists of:
- **Frontend (Streamlit App):**  
  A user interface to display news summaries, sentiment analysis, and comparative analysis. Users can select a company from a dropdown, view detailed summaries, and listen to a Hindi text-to-speech (TTS) version of the news.
  
- **Backend (Flask API):**  
  A REST API to serve news data in JSON format. This API is used by the frontend to fetch the processed news summary and analysis.

## Processing Steps

### 1. News Extraction
- **Objective:** Extract news articles related to companies (Tesla, Amazon, Google, JP Morgan) using the NewsAPI.
- **Key Tasks:**
  - Fetch at least 10 articles per company.
  - Use tools like `newspaper3k` to scrape the full content from article URLs.
  - Store the extracted data (title, summary, content) in a structured format.

### 2. Preprocessing
- **Objective:** Clean and prepare the raw news articles for analysis.
- **Key Tasks:**
  - Remove unwanted characters, URLs, and extra whitespace.
  - Handle truncated content (e.g., removing placeholders like `[...]`).
  - Filter out rows with empty or meaningless content.

### 3. News Summarization
- **Objective:** Generate concise summaries of the articles.
- **Key Tasks:**
  - Use an abstractive summarization model (e.g., T5 or BART) from the `transformers` library.
  - Truncate long articles to meet model input limits.
  - Store summaries along with metadata in a structured format.

### 4. Topic Extraction
- **Objective:** Identify key topics from the summarized articles.
- **Key Tasks:**
  - Extract relevant keywords and keyphrases using tools like **KeyBERT**.
  - Group and integrate extracted topics with other metadata.

### 5. Sentiment Analysis
- **Objective:** Determine the overall tone of each news article.
- **Key Tasks:**
  - Use a fine-tuned sentiment analysis model (e.g., DistilBERT) to classify summaries as Positive, Negative, or Neutral.
  - Aggregate sentiment labels to produce an overall sentiment distribution per company.

### 6. Text-to-Speech (TTS)
- **Objective:** Convert the summarized text into natural-sounding Hindi speech.
- **Key Tasks:**
  - Translate English summaries to Hindi (if required) using libraries like `googletrans`.
  - Use `gTTS` to generate Hindi speech from the summaries.
  - Save the generated audio as MP3 files, one per company.

### 7. Comparative Analysis
- **Objective:** Combine and compare the processed data for each company.
- **Key Tasks:**
  - Aggregate data from multiple articles (title, summary, sentiment, topics).
  - Calculate sentiment distribution and perform pairwise coverage differences.
  - Identify common and unique topics.
  - Format the final analysis as a JSON file.

## Frontend

The frontend is implemented using Streamlit:
- **File:** `app.py`
- **Features:**
  - Displays a dropdown with available company names (extracted from the CSV file).
  - Shows the news summary and analysis (loaded from `comparative_sentiment_analysis.json`).
  - Plays the corresponding Hindi TTS audio if available.
  
### Running the Frontend
1. Ensure all required packages are installed (see `requirements.txt`).
2. Run the Streamlit app:
   ```bash
   streamlit run app.py
