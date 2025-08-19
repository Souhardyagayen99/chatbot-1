from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
from config import GEMINI_API_KEY
import json

app = Flask(__name__)
CORS(app)

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-pro')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Get response from Gemini
        response = model.generate_content(user_message)
        
        return jsonify({
            'response': response.text,
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({
            'error': f'An error occurred: {str(e)}',
            'status': 'error'
        }), 500

@app.route('/api/health')
def health():
    return jsonify({'status': 'healthy', 'model': 'gemini-1.5-pro'})

if __name__ == '__main__':
    print("🚀 Starting Gemini 2.5 Pro Chatbot Web Server...")
    print("📱 Open your browser and go to: http://localhost:5000")
    print("🔧 API endpoint: http://localhost:5000/api/chat")
    print("💚 Health check: http://localhost:5000/api/health")
    print("-" * 50)
    
    app.run(debug=True, host='0.0.0.0', port=5000) 