from flask import Flask, request, jsonify, render_template
from model import get_ai_response
import time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    user_message = data.get('message')

    if not user_message:
        return jsonify({'error': 'Missing message content'}), 400

    system_prompt = "You are an AI assistant helping with customer inquiries. Provide a helpful and concise response."

    start_time = time.time()

    try:
        result = get_ai_response(system_prompt, user_message)
        result['duration'] = round(time.time()-start_time, 2)
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)