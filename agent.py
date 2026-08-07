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

from assistant_router import AssistantRouter


from commands import handle_task_command

from file_operations import(
    find_and_open,
    list_files,
    create_folder,
)

from progress import(create_progress_table)

from knowledge_base import create_knowledge_table

from desktop_control import open_application,close_application

from config import SEARCH_PATH,DOCUMENTS,DESKTOP

from datetime import datetime

def log(message: str) -> None:
    now = datetime.now().strftime("%H:%M:%S")
    print(f"[{now}] {message}")

load_dotenv()
import os

# Startup
log("=" * 40)
log("Starting SanX Assistant V1")

if os.getenv("GOOGLE_API_KEY"):
    log("✓ Google API Key Loaded Successfully.")
else:
    log("✗ Google API Key Not Find")

# Initialize database
init_db()
save_preferences("Sanx", "bunk")
create_progress_table()
create_knowledge_table()

log("✓ Database Ready")
log("✓ Progress Ready")
log("✓ Knowledge Base Ready")
log("=" * 40)

# Create the router
router = AssistantRouter()


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

    @staticmethod
    async def process_command(session, command: str) -> bool:

        command = command.lower().strip().strip(".,!?")

        # File Commands

        if "show file" in command or "show files" in command or "list files" in command:
            files = list_files(DOCUMENTS)
        
            await session.generate_reply(
                instructions=f"Files found: {files}"
            )
            return True
        
        # Open Applications/files

        if (
            command.startswith("open ")
            or command.startswith("launch ")
            or command.startswith("start ")
            or command.startswith("run ")
        ):

            for word in ("open", "launch", "start", "run", "file"):
                command = command.replace(word, "")

            name = command.strip()

            
            SUPPORTED_APPS = {
                "chrome",
                "notepad",
                "calculator",
                "paint",
                "explorer",
                "file explorer",
                "cmd",
                "youtube",
                "google",
                "github"
            }

            if name == "file explorer":
                name = "explorer"

            print(f"APP NAME = {repr(name)}")

            if name in SUPPORTED_APPS:
                try:
                    result = open_application(name)
                except Exception as e:
                    result = f"Sorry Sanx, I couldn't open {name}. Error: {e}"
            else:
                try:
                    result = find_and_open(name, SEARCH_PATH)
                except Exception as e:
                    result = f"Sorry Sanx, I couldn't find or open {name}. Error: {e}"

            log(f"[OPEN]{result}")

            await session.generate_reply(
                instructions=result
            )

            return True

        #Close Applications

        if (
            command.startswith("close ")
            or command.startswith("exit ")
            or command.startswith("quit ")
            or command.startswith("stop ")
        ):

            for word in ("close", "exit", "quit", "stop"):
                command = command.replace(word, "")

            name = command.strip()

            if name == "file explorer":
                name = "explorer"

            result = close_application(name)

            log(f"[CLOSE]{result}")

            await session.generate_reply(
                instructions=result
            )

            return True
        
        #Folder Commands

        if "create folder" in command:
            result = create_folder(
                os.path.join(DESKTOP,"SanX Folder")
            )

            await session.generate_reply(
                instructions=result
            )
            return True

        # Help Command

        if command in ["help", "commands", "what can you do"]:

            help_text = """
            Available SanX Commands

            📂 File Commands
            • show files
            • open <file name>
            • create folder

            🖥️ Application Commands
            • open chrome
            • open github
            • open youtube
            • open notepad
            • open calculator
            • open paint
            • open cmd
            • open file explorer

            ❌ Close Commands
            • close chrome
            • close notepad
            • close calculator
            • close paint
            • close cmd

            📝 Task Commands
            • add task
            • show tasks
            • complete task
            • delete task

            🎓 Study Commands
            • study <topic>
            • quiz <topic>

            💼 Placement
            • placement interview
            """

            await session.generate_reply(
                instructions=help_text
            )

            return True


        # Task Commands

        task_result = handle_task_command(command)
        if task_result:
            log(f"[TASK]{task_result}")
            return True


        # App Router

        result = router.route(command)
        if result:
            log(f"[SANX]{result}")
            return True


        return False
     


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

    from livekit.agents import UserInputTranscribedEvent
    import asyncio

    @session.on("user_input_transcribed")
    def on_user_input(event):
        asyncio.create_task(handle_user_input(event))

    async def handle_user_input(event):
        if not event.is_final:
            return

        command = event.transcript.strip()
        print(f"User: {command}")

        # Try local commands first
        handled = await SanxAssistant.process_command(session, command)

        if handled:
            print("Local command executed.")
            return

        # If not handled locally, ask Gemini
        await session.generate_reply(
            instructions=f"User said: {command}"
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