from dotenv import load_dotenv
from livekit import agents
from livekit.agents import Agent, AgentSession
from livekit.plugins import openai, silero

load_dotenv()


class VoiceAssistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions=(
                "You are a friendly and helpful AI voice assistant. "
                "Be warm, engaging, and helpful."
            )
        )


async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        stt=openai.STT(),
        llm=openai.LLM(model="gpt-4o-mini"),
        tts=openai.TTS(voice="nova"),
        vad=silero.VAD.load(),
    )
    
    await session.start(
        room=ctx.room,
        agent=VoiceAssistant(),
    )
    
    await session.generate_reply(
        instructions="Greet the user warmly and ask how you can help them today. Ask how they are doing, and be empathetic."
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))