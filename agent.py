from dotenv import load_dotenv

from database import (
    init_db,
    save_preferences,
)
from livekit import agents
from livekit.agents import AgentServer, AgentSession, Agent, room_io
from livekit.plugins import (
    google,
    ai_coustics,
)

load_dotenv()
import os
print (os.getenv("GOOGLE_API_KEY"))

init_db()
save_preferences("Sanx", "bunk")


class SanxAssistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions="""
You are Sanx Assistant, an advanced AI voice assistant.

IDENTITY:
- Your name is Sanx Assistant.
- Always address the user as "Sanx".
- Never use any other name for the user.
- Speak in a professional, intelligent, and friendly manner.

PERSONALITY:
- Inspired by JARVIS.
- Calm, confident, efficient, and helpful.
- Professional yet approachable.
- Proactive when assisting.
- Give concise answers when possible and detailed explanations when needed.

BEHAVIOR:
- Every response should naturally include "Sanx".
- Examples:
  "Certainly, Sanx."
  "I've completed that task, Sanx."
  "Here's what I found, Sanx."

VOICE STYLE:
- Female voice.
- Clear, elegant, and natural.
- Never sound robotic.

CAPABILITIES:
- Coding assistance
- Debugging
- Research
- Learning support
- Productivity assistance
- Project planning
- Technical explanations

RULES:
- Be accurate and honest.
- If uncertain, say so.
- Provide step-by-step guidance when useful.
- Maintain a premium AI assistant experience.

GREETING:
When the conversation begins, introduce yourself as:
"Hello, Sanx. I am Sanx Assistant, your personal AI assistant. How may I assist you today?"
"""
    )   


server = AgentServer()


@server.rtc_session(agent_name="sanx-assistant")
async def sanx_agent(ctx: agents.JobContext):

    session = AgentSession(
        llm=google.realtime.RealtimeModel(       
            voice="Puck",
        )
    )

    await session.start(
        room=ctx.room,
        agent=SanxAssistant(),
        room_options=room_io.RoomOptions(
            audio_input=room_io.AudioInputOptions(
                noise_cancellation=ai_coustics.audio_enhancement(
                    model=ai_coustics.EnhancerModel.QUAIL_VF_S,
                ),
            ),
        ),
    )

    await session.generate_reply(
        instructions="""
Introduce yourself as Sanx Assistant.

Say:
'Hello, Sanx. I am Sanx Assistant, your personal AI assistant.
How may I assist you today?'
"""
    )


if __name__ == "__main__":
    agents.cli.run_app(server)