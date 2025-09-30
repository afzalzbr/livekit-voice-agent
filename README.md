# LiveKit Voice Agent 🎙️

A friendly and helpful AI voice assistant built with LiveKit and OpenAI. This agent provides real-time voice interaction using advanced speech recognition, language modeling, and text-to-speech capabilities.

## 🚀 Features

- **Real-time Voice Interaction**: Seamless voice conversations with low latency
- **OpenAI Integration**: Powered by OpenAI's latest models
  - **Speech-to-Text**: Whisper for accurate speech recognition
  - **Language Model**: GPT-4o-mini for intelligent responses
  - **Text-to-Speech**: High-quality voice synthesis with "nova" voice
- **Voice Activity Detection**: Silero VAD for natural conversation flow
- **Empathetic AI**: Warm, engaging, and helpful personality
- **Real-time Processing**: Built on LiveKit's robust real-time infrastructure

## 📋 Prerequisites

- Python 3.8 or higher
- LiveKit Cloud account or self-hosted LiveKit server
- OpenAI API key

## 🛠️ Installation

1. **Clone the repository** (or download the files)
   ```bash
   git clone https://github.com/afzalzbr/livekit-voice-agent.git
   cd livekit-voice-agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp env.example .env
   ```
   
   Edit the `.env` file with your credentials:
   ```env
   # LiveKit Configuration
   LIVEKIT_URL="wss://your-livekit-server.cloud"
   LIVEKIT_API_KEY="your_api_key_here"
   LIVEKIT_API_SECRET="your_api_secret_here"
   
   # OpenAI Configuration
   OPENAI_API_KEY="sk-your_openai_key_here"
   ```

## 🔧 Configuration

### LiveKit Setup

1. **Create a LiveKit Cloud account** at [livekit.io](https://livekit.io)
2. **Get your credentials** from the LiveKit dashboard
3. **Update your `.env`** file with the LiveKit URL, API key, and secret

### OpenAI Setup

1. **Get an OpenAI API key** from [platform.openai.com](https://platform.openai.com)
2. **Add your API key** to the `.env` file

## 🏃‍♂️ Usage

### Running the Agent

Start the voice agent worker:

```bash
python agent.py
```

The agent will:
1. Initialize with OpenAI and Silero configurations
2. Wait for room connections
3. Start voice interaction sessions
4. Provide empathetic greetings and assistance

### Connecting to the Agent

The agent runs as a LiveKit worker and will handle incoming room connections. You can connect to it using:

- **LiveKit Web SDK**: Build a web interface
- **LiveKit Mobile SDKs**: iOS/Android applications
- **LiveKit Playground**: For testing purposes

### Example Interaction Flow

1. **User joins** the LiveKit room
2. **Agent detects** the participant
3. **Agent greets** the user warmly
4. **Conversation begins** with natural voice interaction
5. **Agent responds** empathetically to user queries

## 📁 Project Structure

```
livekit-voice-agent/
├── agent.py              # Main voice agent implementation
├── requirements.txt       # Python dependencies
├── env.example           # Environment variables template
├── .env                  # Your environment variables (create this)
└── README.md            # This file
```

## 🔍 Code Overview

### Main Components

- **`VoiceAssistant` Class**: Extends LiveKit's Agent class with custom instructions
- **`entrypoint` Function**: Configures and starts the agent session
- **OpenAI Integration**: STT, LLM, and TTS powered by OpenAI
- **Silero VAD**: Voice activity detection for natural conversations

### Key Technologies

- **LiveKit Agents**: Real-time agent framework
- **OpenAI Whisper**: Speech-to-text conversion
- **OpenAI GPT-4o-mini**: Language understanding and generation
- **OpenAI TTS**: Text-to-speech synthesis
- **Silero VAD**: Voice activity detection

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**
   ```bash
   # Make sure all dependencies are installed
   pip install -r requirements.txt
   ```

2. **Environment Variables**
   ```bash
   # Verify your .env file exists and has the correct values
   cat .env
   ```

3. **LiveKit Connection Issues**
   - Check your LiveKit URL format (should start with `wss://`)
   - Verify your API key and secret are correct
   - Ensure your LiveKit server is running

4. **OpenAI API Issues**
   - Verify your OpenAI API key is valid
   - Check your OpenAI account has sufficient credits
   - Ensure you have access to the required models

### Logging

The agent includes comprehensive logging to help with debugging:

```python
# Logs are configured in agent.py
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

Check the console output for detailed information about:
- Agent initialization
- Session configuration
- Room connections
- Greeting delivery

## 🔧 Customization

### Changing the AI Personality

Edit the instructions in the `VoiceAssistant` class:

```python
super().__init__(
    instructions=(
        "Your custom personality instructions here..."
    )
)
```

### Using Different Models

Modify the session configuration:

```python
session = AgentSession(
    stt=openai.STT(),
    llm=openai.LLM(model="gpt-4"),  # Change model here
    tts=openai.TTS(voice="alloy"),  # Change voice here
    vad=silero.VAD.load(),
)
```

### Custom Greeting

Update the greeting generation:

```python
await session.generate_reply(
    instructions="Your custom greeting instructions here..."
)
```

## 📝 License

This project is part of a take-home assignment for Fortell AI.

## 🤝 Contributing

This is a demonstration project. For improvements or questions, please reach out to the development team.

## 📞 Support

For technical support or questions:
- Check the [LiveKit Documentation](https://docs.livekit.io)
- Review the [OpenAI API Documentation](https://platform.openai.com/docs)
- Examine the console logs for debugging information

---

**Happy voice chatting! 🎉**