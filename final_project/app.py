from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-response", methods=["POST"])
def get_response():
    user_message = request.json.get("message")

    # Simple predefined responses
    responses = {
        "hello": "Hello! How can I help you?",
        "bye": "Goodbye! Have a great day!",
        "how are you": "I'm a bot, so I don't have feelings, but I'm here to help you!"
    }

    # Return a response based on user input
    return jsonify({"response": responses.get(user_message.lower(), "I don't understand.")})

if __name__ == "__main__":
    app.run(debug=True)