# Gemini Chatbot

A simple Python chatbot powered by Google's Gemini AI API.

## Features

- 🤖 Powered by Google Gemini AI
- 💬 Interactive command-line interface
- 🔄 Conversation memory (maintains chat history)
- 🛡️ Error handling and graceful exits

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the chatbot:**
   ```bash
   python chatbot.py
   ```

## Usage

- Type your messages and press Enter to chat
- Type `quit`, `exit`, or `bye` to end the conversation
- Press `Ctrl+C` to exit at any time

## Example Conversation

```
🤖 Welcome to Gemini Chatbot!
Type 'quit' or 'exit' to end the conversation.
--------------------------------------------------

👤 You: Hello! How are you today?

🤖 Chatbot: Hello! I'm doing well, thank you for asking. I'm here and ready to help you with any questions or tasks you might have. How can I assist you today?

👤 You: What's the weather like?

🤖 Chatbot: I don't have access to real-time weather information, but I can help you with many other topics! Is there something specific you'd like to know about or discuss?

👤 You: quit

🤖 Chatbot: Goodbye! Have a great day!
```

## Files

- `chatbot.py` - Main chatbot application
- `config.py` - Configuration file with API key
- `requirements.txt` - Python dependencies
- `README.md` - This file

## Note

The API key is included in the `config.py` file for demonstration purposes. In a production environment, you should use environment variables or a secure configuration management system. 