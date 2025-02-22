from flask import Flask, request, jsonify
from flask_cors import CORS
import ollama

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('content', '')

    if not user_message:
        return jsonify({'message': {'content': 'No message provided'}}), 400

    response = ollama.chat(model='llama3', messages=[{
        'role': 'user',
        'content': user_message
    }])

    return jsonify({'message': {'content': response['message']['content']}})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)