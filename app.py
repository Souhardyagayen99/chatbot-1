from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
from config import GEMINI_API_KEY
import json

app = Flask(__name__)
# Limit upload size to 16 MB
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
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
        # Handle multipart form-data (message + optional file)
        if request.content_type and request.content_type.startswith('multipart/form-data'):
            user_message = request.form.get('message', '').strip()
            upload = request.files.get('file')

            if not user_message and not upload:
                return jsonify({'error': 'No message or file provided'}), 400

            # If a file is attached, handle based on MIME type
            if upload and upload.filename:
                mime_type = (upload.mimetype or '').lower()

                # Images: send multimodal content to the model
                if mime_type.startswith('image/'):
                    image_part = { 'mime_type': mime_type, 'data': upload.read() }
                    parts = []
                    if user_message:
                        parts.append(user_message)
                    parts.append(image_part)
                    response = model.generate_content(parts)
                # Text-like files: read content and prepend to the prompt
                elif mime_type.startswith('text/') or upload.filename.lower().endswith((
                    '.txt', '.md', '.csv', '.json'
                )):
                    file_bytes = upload.read()
                    file_text = file_bytes.decode('utf-8', errors='ignore')
                    prompt = user_message or 'Please analyze the attached file.'
                    combined = f"{prompt}\n\nAttached file content (truncated if large):\n{file_text}"
                    response = model.generate_content(combined)
                else:
                    return jsonify({'error': 'Unsupported file type. Please upload an image or text file.'}), 400
            else:
                # No file attached, just process the message
                if not user_message:
                    return jsonify({'error': 'No message provided'}), 400
                response = model.generate_content(user_message)

            return jsonify({'response': response.text, 'status': 'success'})

        # Handle JSON body (no file)
        data = request.get_json(silent=True) or {}
        user_message = data.get('message', '').strip()
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400

        response = model.generate_content(user_message)
        return jsonify({'response': response.text, 'status': 'success'})

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}', 'status': 'error'}), 500

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