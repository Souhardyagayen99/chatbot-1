import google.generativeai as genai
from config import GEMINI_API_KEY
import sys

class Chatbot:
    def __init__(self):
        # Configure the Gemini API
        genai.configure(api_key=GEMINI_API_KEY)
        
        # Initialize the model
        self.model = genai.GenerativeModel('gemini-2.0-flash-exp')
        self.chat = self.model.start_chat(history=[])
        
        print("🤖 Welcome to Gemini Chatbot!")
        print("Type 'quit' or 'exit' to end the conversation.")
        print("-" * 50)
    
    def get_response(self, user_input):
        """Get response from Gemini AI"""
        try:
            response = self.chat.send_message(user_input)
            return response.text
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"
    
    def run(self):
        """Main chat loop"""
        while True:
            try:
                # Get user input
                user_input = input("\n👤 You: ").strip()
                
                # Check for exit commands
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    print("\n🤖 Chatbot: Goodbye! Have a great day!")
                    break
                
                # Skip empty inputs
                if not user_input:
                    continue
                
                # Get and display response
                print("\n🤖 Chatbot: ", end="")
                response = self.get_response(user_input)
                print(response)
                
            except KeyboardInterrupt:
                print("\n\n🤖 Chatbot: Goodbye! Have a great day!")
                break
            except Exception as e:
                print(f"\n❌ Error: {str(e)}")

def main():
    """Main function to run the chatbot"""
    try:
        chatbot = Chatbot()
        chatbot.run()
    except Exception as e:
        print(f"Failed to initialize chatbot: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 