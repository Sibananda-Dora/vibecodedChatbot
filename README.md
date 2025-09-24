# Gemini 2.5 Flash Chatbot

A simple yet powerful chatbot interface using Google's Gemini 2.5 Flash API.

## Features

-  **Gemini 2.5 Flash Integration**: Powered by Google's latest AI model
- **Real-time Chat**: Instant responses with loading indicators

## Setup Instructions

### 1. Get Your Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key (it's free!)
4. Copy your API key

### 2. Install Dependencies

```bash
# Install Python dependencies
pip install -r requirements.txt
```

### 3. Configure Environment

1. Open the `.env` file in your project directory
2. Replace `your_gemini_api_key_here` with your actual API key:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

### 4. Run the Application

```bash
python main.py
```

### Web Interface
1. Choose option 1 (or just press Enter)
2. Open your browser and go to http://127.0.0.1:5000
3. Start chatting with Gemini!

## Contributing

Feel free to submit issues and pull requests to improve the chatbot!