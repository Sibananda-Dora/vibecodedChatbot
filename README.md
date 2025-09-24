# Gemini 2.5 Flash Chatbot

A simple yet powerful chatbot interface using Google's Gemini 2.5 Flash API with both web and console interfaces.

## Features

- 🤖 **Gemini 2.5 Flash Integration**: Powered by Google's latest AI model
- 💻 **Dual Interface**: Choose between web UI or console mode
- 🎨 **Beautiful Web UI**: Modern, responsive chat interface
- ⚡ **Real-time Chat**: Instant responses with loading indicators
- 🔒 **Secure**: API key stored in environment variables

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

You'll be prompted to choose between:
- **Web Interface** (default): Opens a beautiful web UI at http://127.0.0.1:5000
- **Console Mode**: Simple command-line chat interface

## Usage

### Web Interface
1. Choose option 1 (or just press Enter)
2. Open your browser and go to http://127.0.0.1:5000
3. Start chatting with Gemini!

### Console Mode
1. Choose option 2
2. Type your messages directly in the terminal
3. Type 'quit', 'exit', or 'q' to end the conversation

## Files Structure

```
├── main.py              # Main application file
├── requirements.txt     # Python dependencies
├── .env                # Environment variables (API key)
├── templates/
│   └── index.html      # Web interface template
└── README.md           # This file
```

## Features of the Web Interface

- **Responsive Design**: Works on desktop and mobile
- **Real-time Chat**: Messages appear instantly
- **Loading Indicators**: Shows when AI is thinking
- **Error Handling**: Graceful error messages
- **Auto-scroll**: Always shows latest messages
- **Keyboard Shortcuts**: Press Enter to send messages

## Troubleshooting

### "GEMINI_API_KEY not found"
- Make sure your `.env` file has the correct API key
- Ensure there are no spaces around the `=` sign
- Verify your API key is valid at Google AI Studio

### "Failed to connect to the server"
- Check if the Flask server is running
- Ensure no other application is using port 5000
- Try refreshing the web page

### Module Not Found Errors
- Run `pip install -r requirements.txt` again
- Make sure you're using the correct Python environment

## License

MIT License - Feel free to use and modify!

## Contributing

Feel free to submit issues and pull requests to improve the chatbot!