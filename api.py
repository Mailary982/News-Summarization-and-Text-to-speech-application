from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# ✅ Load the JSON data
file_path = os.path.join(os.getcwd(), "comparative_sentiment_analysis.json")

with open(file_path, "r", encoding="utf-8") as f:
    news_data = json.load(f)

@app.route('/get_news', methods=['GET'])
def get_news():
    """Fetch news data for a given company"""
    company_name = request.args.get("company", "").lower()

    for company in news_data:
        if company["Company"].lower() == company_name:
            return jsonify(company)  # Return JSON response

    return jsonify({"error": "Company not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run Flask on port 5000
