from dotenv import load_dotenv

from database import (
    init_db,
    save_preferences,
    create_progress_table,
)
from livekit import agents
from livekit.agents import AgentServer, AgentSession, Agent, room_io
from livekit.plugins import (
    google,
    ai_coustics,
)

from study import study_mode
from quiz import get_quiz
from placement import interview_mode
from progress import (
    create_progress_table,
    save_progress,
    get_progress
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
    
def process_command(command):

    command = command.lower()

    if command.startswith("study "):
        topic = command.replace("study ", "")
        return study_mode(topic)

    elif command.startswith("quiz "):
        subject = command.replace("quiz ", "")
        quiz = get_quiz(subject)

        return f"""
Question:
{quiz['question']}

(Answer: {quiz['answer']})
"""

    elif command.startswith("interview "):
        category = command.replace("interview ", "")
        return interview_mode(category)

    elif command == "progress":

        rows = get_progress()

        if not rows:
            return "No study progress found."

        result = "Study Progress\n\n"

        for row in rows:

            result += (
                f"Topic: {row[0]}\n"
                f"Status: {row[1]}\n"
                f"Score: {row[2]}/10\n"
                f"Date: {row[3]}\n\n"
            )

        return result

    else:
        return None       


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