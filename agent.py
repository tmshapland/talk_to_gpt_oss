from dotenv import load_dotenv

from livekit import agents
from livekit.agents import AgentSession, Agent
from livekit.plugins import (
    groq,
    cartesia,
    assemblyai,
    noise_cancellation,
    silero,
)
from livekit.plugins.turn_detector.english import EnglishModel
from utils import load_prompt

load_dotenv()


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions=
        load_prompt('prompt.yaml')
        )


async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        stt=assemblyai.STT(),
        llm=groq.LLM(model="openai/gpt-oss-20b"),
        tts=cartesia.TTS(model="sonic-2", voice="f786b574-daa5-4673-aa0c-cbe3e8534c02"),
        vad=silero.VAD.load(),
        turn_detection=EnglishModel(),
    )


    await session.start(
        room=ctx.room,
        agent=Assistant(),

    )

    await session.say("I am G P T O S S. Nice to meet you. A M A.")


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))