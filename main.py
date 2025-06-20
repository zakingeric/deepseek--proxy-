from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DEEPSEEK_API_KEY = "sk-8686f6e5d794407c84cccebe1235f476"
DEEPSEEK_URL = "https://api.deepseek.com/v1/chat/completions"

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    response = requests.post(DEEPSEEK_URL, headers={
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }, json=data)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)￼Enter
