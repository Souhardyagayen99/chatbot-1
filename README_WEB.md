# 🤖 Gemini 2.0 Chatbot Web Application

A modern, responsive web interface for your Gemini 2.0 AI chatbot powered by Google's latest AI model.

## ✨ Features

- **Modern UI**: Beautiful, responsive design with gradient backgrounds and smooth animations
- **Real-time Chat**: Instant responses from Gemini 2.0 Flash Experimental model
- **Mobile Friendly**: Optimized for both desktop and mobile devices
- **Typing Indicators**: Visual feedback when the AI is processing your request
- **Error Handling**: Graceful error handling with user-friendly messages
- **API Endpoints**: RESTful API for integration with other applications

## 🚀 Quick Start

### Option 1: Automatic Setup (Recommended)
```bash
python run_web.py
```

This script will:
- Install all required dependencies
- Start the Flask web server
- Open your browser to the application

### Option 2: Manual Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Start the web server
python app.py
```

## 🌐 Access the Application

Once running, open your web browser and navigate to:
- **Main Application**: http://localhost:5000
- **API Endpoint**: http://localhost:5000/api/chat
- **Health Check**: http://localhost:5000/api/health

## 🛠️ API Usage

### Chat Endpoint
```bash
POST /api/chat
Content-Type: application/json

{
    "message": "Hello, how are you?"
}
```

### Response Format
```json
{
    "response": "Hello! I'm doing well, thank you for asking. How can I help you today?",
    "status": "success"
}
```

## 📁 Project Structure

```
chatbot-1/
├── app.py                 # Flask web server
├── run_web.py            # Automatic startup script
├── config.py             # Configuration (API keys)
├── chatbot.py            # Original command-line chatbot
├── templates/
│   └── index.html        # Web interface
├── requirements.txt       # Python dependencies
└── README_WEB.md         # This file
```

## 🔧 Configuration

Make sure your `config.py` file contains your Gemini API key:
```python
GEMINI_API_KEY = "your_api_key_here"
```

Get your free API key from: https://aistudio.google.com/

## 🎨 Customization

### Styling
The web interface uses CSS with:
- Gradient backgrounds
- Smooth animations
- Responsive design
- Modern chat bubble layout

### Features
You can easily customize:
- Color schemes in the CSS
- Chat behavior in the JavaScript
- API responses in the Flask backend
- Model parameters in `app.py`

## 🚨 Troubleshooting

### Common Issues

1. **Port already in use**
   - Change the port in `app.py` (line 58)
   - Or stop other services using port 5000

2. **API key errors**
   - Verify your API key in `config.py`
   - Check if you have sufficient API quota

3. **Dependencies not installed**
   - Run: `pip install -r requirements.txt`
   - Or use the automatic setup: `python run_web.py`

### Debug Mode
The Flask app runs in debug mode by default. To disable:
```python
app.run(debug=False, host='0.0.0.0', port=5000)
```

## 🔒 Security Notes

- The web server runs on localhost by default
- API key is stored in `config.py` (keep this file secure)
- Consider using environment variables for production deployment

## 📱 Mobile Support

The web interface is fully responsive and works on:
- Desktop browsers
- Mobile browsers
- Tablets
- All modern devices

## 🎯 Next Steps

- Add user authentication
- Implement chat history storage
- Add file upload capabilities
- Integrate with databases
- Deploy to production servers

## 🤝 Contributing

Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve the documentation

---

**Enjoy chatting with Gemini 2.0! 🚀** 