from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
API_TOKEN = "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"  # 🔁 Replace with real token

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

@app.route('/generate-image', methods=['POST'])
def generate_image():
    data = request.get_json()
    prompt = data.get("prompt", "")

    payload = {
        "inputs": prompt
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    result = response.json()

    if isinstance(result, dict) and result.get("error"):
        return jsonify({"error": result["error"]})

    # Some models return image base64 or URLs — adjust accordingly
    return jsonify({"url": result[0]["generated_image"]})

if __name__ == '__main__':
    app.run(debug=True)
