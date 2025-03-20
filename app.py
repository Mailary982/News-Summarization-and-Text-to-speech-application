import streamlit as st
import os
import json

JSON_FILE_PATH = "comparative_sentiment_analysis.json"

st.title("📢 News Sentiment Analysis")

# Check if JSON file exists and load it
if not os.path.exists(JSON_FILE_PATH):
    st.error("JSON file not found! Please run the data processing script first.")
    st.stop()
else:
    with open(JSON_FILE_PATH, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            st.error("Error reading JSON file! Ensure it's correctly formatted.")
            st.stop()

# Assuming the JSON is a dictionary with company names as keys
companies = list(data.keys())
if not companies:
    st.error("No companies found in the JSON file.")
    st.stop()

# Display the companies in a dropdown (selectbox)
default_index = companies.index("Tesla") if "Tesla" in companies else 0
company = st.selectbox("Select a company:", companies, index=default_index)

if st.button("Get News Summary"):
    company_data = data.get(company)

    if company_data:
        st.subheader(f"📊 News Summary for {company}")
        st.json(company_data)  # Display the full JSON response for the selected company

        # Extract audio file info
        audio_path = company_data.get("Audio", "").strip()

        # Check if the audio file exists locally
        if audio_path and os.path.exists(audio_path):
            st.subheader("🎧 Listen to Hindi Summary")
            st.audio(audio_path)
        else:
            st.warning(f"Audio file not found: {audio_path}")
    else:
        st.error(f"No data found for '{company}'. Try another company.")
