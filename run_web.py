#!/usr/bin/env python3
"""
Startup script for Gemini 2.0 Chatbot Web Application
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Packages installed successfully!")
    except subprocess.CalledProcessError:
        print("❌ Failed to install packages. Please run manually:")
        print("   pip install -r requirements.txt")
        return False
    return True

def run_flask_app():
    """Run the Flask application"""
    print("🚀 Starting Flask web server...")
    try:
        subprocess.run([sys.executable, "app.py"])
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except Exception as e:
        print(f"❌ Error running Flask app: {e}")

def main():
    print("🤖 Gemini 2.0 Chatbot Web Application")
    print("=" * 50)
    
    # Check if requirements are installed
    try:
        import flask
        import flask_cors
        print("✅ All required packages are already installed!")
    except ImportError:
        if not install_requirements():
            return
    
    print("\n🌐 Starting web application...")
    print("📱 Open your browser and go to: http://localhost:5000")
    print("🔧 API endpoint: http://localhost:5000/api/chat")
    print("💚 Health check: http://localhost:5000/api/health")
    print("⏹️  Press Ctrl+C to stop the server")
    print("-" * 50)
    
    run_flask_app()

if __name__ == "__main__":
    main() 