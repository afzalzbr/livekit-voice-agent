# LiveKit Voice Agent 🎙️

A comprehensive voice AI solution featuring both a Python backend agent and a modern Next.js frontend interface. This project provides real-time voice interaction using advanced speech recognition, language modeling, and text-to-speech capabilities.

## 🌐 Live Demo

**Try the voice agent right now!** Visit the live demo at: [https://livekit-voice-agent-demo.vercel.app/](https://livekit-voice-agent-demo.vercel.app/)

The demo showcases all the features including real-time voice interaction, chat interface, and responsive design.

## 🚀 Features

### Backend (Python Agent)

- **Real-time Voice Interaction**: Seamless voice conversations with low latency
- **OpenAI Integration**: Powered by OpenAI's latest models
  - **Speech-to-Text**: Whisper for accurate speech recognition
  - **Language Model**: GPT-4o-mini for intelligent responses
  - **Text-to-Speech**: High-quality voice synthesis with "nova" voice
- **Voice Activity Detection**: Silero VAD for natural conversation flow
- **Empathetic AI**: Warm, engaging, and helpful personality
- **Real-time Processing**: Built on LiveKit's robust real-time infrastructure

### Frontend (Next.js Web Interface)

- **Modern Web Interface**: Built with Next.js 15 and React 19
- **Real-time Voice Interaction**: LiveKit Web SDK integration
- **Camera Video Streaming**: Support for video input
- **Screen Sharing**: Share your screen during conversations
- **Audio Visualization**: Real-time audio level monitoring
- **Chat Interface**: Text-based communication alongside voice
- **Theme Support**: Light/dark mode with system preference detection
- **Responsive Design**: Works on desktop and mobile devices

## 📋 Prerequisites

- **Python 3.8 or higher** (for the backend agent)
- **Node.js 18+ and pnpm** (for the frontend)
- **LiveKit Cloud account** or self-hosted LiveKit server
- **OpenAI API key**

## 🛠️ Installation

1. **Clone the repository** (or download the files)

   ```bash
   git clone https://github.com/afzalzbr/livekit-voice-agent.git
   cd livekit-voice-agent
   ```

2. **Install Python dependencies (Backend)**

   ```bash
   pip install -r requirements.txt
   ```

3. **Install Node.js dependencies (Frontend)**

   ```bash
   cd agent-frontend-nextjs
   pnpm install
   cd ..
   ```

4. **Set up environment variables**

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

5. **Configure LiveKit project settings**

   Update `livekit.toml` with your project details:

   ```toml
   [project]
     subdomain = "your-livekit-subdomain"

   [agent]
     id = "your-agent-id"
   ```

## 🔧 Configuration

### LiveKit Setup

1. **Create a LiveKit Cloud account** at [livekit.io](https://livekit.io)
2. **Get your credentials** from the LiveKit dashboard
3. **Update your `.env`** file with the LiveKit URL, API key, and secret
4. **Update `livekit.toml`** with your project subdomain and agent ID

### OpenAI Setup

1. **Get an OpenAI API key** from [platform.openai.com](https://platform.openai.com)
2. **Add your API key** to the `.env` file

### Frontend Configuration

The frontend can be customized in `agent-frontend-nextjs/app-config.ts`:

```typescript
export const APP_CONFIG_DEFAULTS: AppConfig = {
  companyName: "LiveKit",
  pageTitle: "LiveKit Voice Agent",
  pageDescription: "A voice agent built with LiveKit",
  supportsChatInput: true,
  supportsVideoInput: true,
  supportsScreenShare: true,
  // ... more configuration options
};
```

## 🏃‍♂️ Usage

### Running the Complete Application

#### Option 1: Development Mode

1. **Start the Python Agent (Backend)**

   ```bash
   python agent.py
   ```

2. **Start the Next.js Frontend (in a new terminal)**

   ```bash
   cd agent-frontend-nextjs
   pnpm dev
   ```

3. **Access the application**
   - Open http://localhost:3000 in your browser
   - The frontend will automatically connect to your LiveKit agent

#### Option 2: Docker Deployment

1. **Build and run with Docker**
   ```bash
   docker build -t livekit-voice-agent .
   docker run -p 3000:3000 --env-file .env livekit-voice-agent
   ```

### What Happens When Running

**Backend Agent:**

1. Initializes with OpenAI and Silero configurations
2. Waits for room connections
3. Starts voice interaction sessions
4. Provides empathetic greetings and assistance

**Frontend Interface:**

1. Connects to LiveKit room
2. Provides real-time voice interaction UI
3. Supports video, screen sharing, and chat
4. Handles device selection and audio controls

### Example Interaction Flow

1. **User opens** the web interface at localhost:3000
2. **User clicks** "Start call" to join the LiveKit room
3. **Agent detects** the participant and greets warmly
4. **Conversation begins** with natural voice interaction
5. **User can** use voice, video, screen share, or text chat
6. **Agent responds** empathetically to all interactions

## 📁 Project Structure

```
livekit-voice-agent/
├── agent.py                    # Main voice agent implementation
├── requirements.txt             # Python dependencies
├── env.example                 # Environment variables template
├── .env                        # Your environment variables (create this)
├── livekit.toml                # LiveKit project configuration
├── Dockerfile                  # Docker configuration for deployment
├── .dockerignore              # Docker ignore file
├── README.md                   # This file
└── agent-frontend-nextjs/      # Next.js frontend application
    ├── app/                    # Next.js app directory
    │   ├── (app)/             # App router pages
    │   ├── api/               # API routes
    │   ├── components/        # Page components
    │   └── globals.css        # Global styles
    ├── components/             # React components
    │   ├── livekit/           # LiveKit-specific components
    │   ├── ui/                # UI components
    │   └── app.tsx            # Main app component
    ├── hooks/                  # Custom React hooks
    ├── lib/                    # Utility functions and types
    ├── public/                 # Static assets
    ├── package.json            # Node.js dependencies
    ├── pnpm-lock.yaml         # Package lock file
    ├── next.config.ts         # Next.js configuration
    ├── tsconfig.json          # TypeScript configuration
    └── app-config.ts          # App configuration
```

## 🔍 Code Overview

### Backend Components

- **`VoiceAssistant` Class**: Extends LiveKit's Agent class with custom instructions
- **`entrypoint` Function**: Configures and starts the agent session
- **OpenAI Integration**: STT, LLM, and TTS powered by OpenAI
- **Silero VAD**: Voice activity detection for natural conversations

### Frontend Components

- **Next.js App Router**: Modern React framework with app directory structure
- **LiveKit Components**: Pre-built React components for voice/video interaction
- **Custom Hooks**: `useConnectionDetails`, `useChatAndTranscription`, `useDebug`
- **UI Components**: Radix UI components with custom styling
- **Theme System**: Light/dark mode support with system preference detection

### Key Technologies

**Backend:**

- **LiveKit Agents**: Real-time agent framework
- **OpenAI Whisper**: Speech-to-text conversion
- **OpenAI GPT-4o-mini**: Language understanding and generation
- **OpenAI TTS**: Text-to-speech synthesis
- **Silero VAD**: Voice activity detection

**Frontend:**

- **Next.js 15**: React framework with App Router
- **React 19**: Latest React with concurrent features
- **LiveKit Web SDK**: Real-time communication
- **TypeScript**: Type-safe development
- **Tailwind CSS**: Utility-first styling
- **Radix UI**: Accessible component primitives

## 🐛 Troubleshooting

### Common Issues

1. **Python Import Errors**

   ```bash
   # Make sure all dependencies are installed
   pip install -r requirements.txt
   ```

2. **Node.js/pnpm Issues**

   ```bash
   # Install pnpm if not available
   npm install -g pnpm

   # Install frontend dependencies
   cd agent-frontend-nextjs
   pnpm install
   ```

3. **Environment Variables**

   ```bash
   # Verify your .env file exists and has the correct values
   cat .env
   ```

4. **LiveKit Connection Issues**

   - Check your LiveKit URL format (should start with `wss://`)
   - Verify your API key and secret are correct
   - Ensure your LiveKit server is running
   - Check `livekit.toml` configuration

5. **OpenAI API Issues**

   - Verify your OpenAI API key is valid
   - Check your OpenAI account has sufficient credits
   - Ensure you have access to the required models

6. **Frontend Connection Issues**
   - Ensure the backend agent is running
   - Check browser console for errors
   - Verify LiveKit credentials in frontend
   - Check if ports 3000 and LiveKit ports are available

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

## 🐳 Docker Deployment

### Building the Docker Image

```bash
docker build -t livekit-voice-agent .
```

### Running with Docker

```bash
# Run with environment file
docker run -p 3000:3000 --env-file .env livekit-voice-agent

# Run with environment variables
docker run -p 3000:3000 \
  -e LIVEKIT_URL="wss://your-livekit-server.cloud" \
  -e LIVEKIT_API_KEY="your_api_key" \
  -e LIVEKIT_API_SECRET="your_api_secret" \
  -e OPENAI_API_KEY="sk-your_openai_key" \
  livekit-voice-agent
```

### Docker Compose (Optional)

Create a `docker-compose.yml` file:

```yaml
version: "3.8"
services:
  voice-agent:
    build: .
    ports:
      - "3000:3000"
    environment:
      - LIVEKIT_URL=${LIVEKIT_URL}
      - LIVEKIT_API_KEY=${LIVEKIT_API_KEY}
      - LIVEKIT_API_SECRET=${LIVEKIT_API_SECRET}
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    env_file:
      - .env
```

## 🔧 Customization

### Backend Customization

#### Changing the AI Personality

Edit the instructions in the `VoiceAssistant` class:

```python
super().__init__(
    instructions=(
        "Your custom personality instructions here..."
    )
)
```

#### Using Different Models

Modify the session configuration:

```python
session = AgentSession(
    stt=openai.STT(),
    llm=openai.LLM(model="gpt-4"),  # Change model here
    tts=openai.TTS(voice="alloy"),  # Change voice here
    vad=silero.VAD.load(),
)
```

#### Custom Greeting

Update the greeting generation:

```python
await session.generate_reply(
    instructions="Your custom greeting instructions here..."
)
```

### Frontend Customization

#### App Configuration

Modify `agent-frontend-nextjs/app-config.ts`:

```typescript
export const APP_CONFIG_DEFAULTS: AppConfig = {
  companyName: "Your Company",
  pageTitle: "Your Voice Agent",
  pageDescription: "Your custom description",
  supportsChatInput: true,
  supportsVideoInput: true,
  supportsScreenShare: true,
  logo: "/your-logo.svg",
  accent: "#your-color",
  startButtonText: "Start Conversation",
};
```

#### Styling

The frontend uses Tailwind CSS. You can customize styles in:

- `agent-frontend-nextjs/app/globals.css` - Global styles
- Component files - Individual component styling

## 📝 License

This project is part of a take-home assignment for Fortell AI.

## 🤝 Contributing

This is a demonstration project. For improvements or questions, please reach out to the development team.

## 📞 Support

For technical support or questions:

- Check the [LiveKit Documentation](https://docs.livekit.io)
- Review the [OpenAI API Documentation](https://platform.openai.com/docs)
- Examine the console logs for debugging information
- Check the [Next.js Documentation](https://nextjs.org/docs) for frontend issues

## 🚀 Quick Start Summary

1. **Install dependencies**: `pip install -r requirements.txt` and `cd agent-frontend-nextjs && pnpm install`
2. **Configure environment**: Copy `env.example` to `.env` and update with your credentials
3. **Update LiveKit config**: Edit `livekit.toml` with your project details
4. **Run backend**: `python agent.py`
5. **Run frontend**: `cd agent-frontend-nextjs && pnpm dev`
6. **Open browser**: Navigate to http://localhost:3000

---

**Happy voice chatting! 🎉**
