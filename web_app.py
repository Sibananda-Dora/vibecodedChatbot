import os
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

class GeminiChatbot:
    def __init__(self):
        # Configure Gemini API
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        # Remove quotes if present
        api_key = api_key.strip('"').strip("'")
        
        genai.configure(api_key=api_key)
        
        # Initialize the model - using correct model name
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        
        # Start a chat session
        self.chat_session = self.model.start_chat(history=[])
    
    def get_response(self, user_input):
        """Get response from Gemini AI"""
        try:
            print(f"[INFO] Sending message to Gemini: {user_input[:50]}...")
            response = self.chat_session.send_message(user_input)
            print(f"[SUCCESS] Received response from Gemini")
            return response.text
        except Exception as e:
            error_msg = f"Gemini API Error: {str(e)}"
            print(f"[ERROR] {error_msg}")
            return error_msg

# Initialize chatbot
try:
    chatbot = GeminiChatbot()
    print("[SUCCESS] Gemini chatbot initialized successfully!")
except ValueError as e:
    print(f"[ERROR] {e}")
    print("Please set your GEMINI_API_KEY in the .env file")
    chatbot = None
except Exception as e:
    print(f"[ERROR] Unexpected error during initialization: {str(e)}")
    print("Please check your API key and internet connection")
    chatbot = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    if not chatbot:
        return jsonify({'error': 'Chatbot not initialized. Please check your API key.'})
    
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data received'})
            
        user_message = data.get('message', '')
        if not user_message.strip():
            return jsonify({'error': 'Empty message'})
        
        print(f"[REQUEST] Received message: {user_message}")
        response = chatbot.get_response(user_message)
        print(f"[RESPONSE] Sending response: {response[:100]}...")
        
        return jsonify({'response': response})
        
    except Exception as e:
        error_msg = f"Server error: {str(e)}"
        print(f"[ERROR] {error_msg}")
        return jsonify({'error': error_msg}), 500

if __name__ == '__main__':
    print("[SERVER] Starting Gemini 2.5 Flash Web Chatbot...")
    print("[SERVER] Open http://127.0.0.1:5000 in your browser")
    print("[SERVER] Press Ctrl+C to stop the server")
    app.run(debug=False, host='127.0.0.1', port=5000)
