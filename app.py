from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# OpenAI API key
openai.api_key = "your_openai_api_key_here"  # Replace with your API key

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    try:
        # Send prompt to ChatGPT
        response = openai.Completion.create(
            engine="text-davinci-003",  # Replace with the appropriate model
            prompt=prompt,
            max_tokens=150
        )
        return jsonify({"response": response["choices"][0]["text"].strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
