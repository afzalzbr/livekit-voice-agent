import logging
from dotenv import load_dotenv
from livekit import agents
from livekit.agents import Agent, AgentSession
from livekit.plugins import openai, silero

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class VoiceAssistant(Agent):
    """
    A friendly and helpful AI voice assistant.
    Using OpenAI for SST(Whisper), LLM(GPT-4o-mini), and TTS.
    """
    
    def __init__(self) -> None:
        super().__init__(
            instructions=(
                "You are a friendly and helpful AI voice assistant. "
                "Be warm, engaging, and helpful."
            )
        )
        logger.info("VoiceAssistant initialized.")


async def entrypoint(ctx: agents.JobContext):
    # Initialize the agent session with OpenAI and Silero plugins
    session = AgentSession(
        stt=openai.STT(),
        llm=openai.LLM(model="gpt-4o-mini"),
        tts=openai.TTS(voice="nova"),
        vad=silero.VAD.load(),
    )

    logger.info("Agent session configured")
    
    # Start the session
    await session.start(
        room=ctx.room,
        agent=VoiceAssistant(),
    )

    logger.info("Agent session started")

    # Generate initial greeting
    await session.generate_reply(
        instructions="Greet the user warmly and ask how you can help them today. Ask how they are doing, and be empathetic."
    )
    logger.info("Initial Greeting Sent")


if __name__ == "__main__":
    logger.info("Starting LiveKit Voice Agent Worker...")
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))