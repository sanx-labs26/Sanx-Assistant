🤖 SanX Assistant

«A personal AI voice assistant built with Python, LiveKit, AI, and SQLite.»

SanX Assistant is an open-source AI voice assistant designed to help with daily tasks, learning, productivity, and placement preparation.

SanX combines voice interaction with useful productivity and study features to create a practical personal assistant.

---

✨ Features

🎙️ AI Voice Assistant

- Natural voice-based interaction
- AI-powered conversations
- Voice input and responses
- Calm and efficient assistant personality

📚 Study Mode

Study different technical subjects with SanX.

Supported topics include:

- Python
- SQL
- Machine Learning

🧠 Quiz Mode

Test your knowledge with subject-based quizzes.

Example:

Quiz Python
Quiz SQL
Quiz Machine Learning

💼 Placement Interview Mode

Practice interviews with different categories:

- HR Interview
- Python Interview
- SQL Interview
- Machine Learning Interview

📊 Progress Tracker

Track your learning progress, including:

- Subject
- Status
- Score
- Date and time

📝 Task Management

Create and manage tasks using voice commands.

Features include:

- Create tasks
- View tasks
- Complete tasks
- Delete tasks
- Task descriptions
- Due dates

🧠 Memory

SanX can store and retrieve conversation history using SQLite.

📄 Document Support

SanX includes document functionality for PDF-based learning and document processing.

🖥️ Desktop & File Operations

SanX can perform selected local operations such as:

- Open applications
- Open files
- Search files
- List files
- Create folders

---

🛠️ Tech Stack

Technology| Purpose
Python| Core programming language
LiveKit Agents| Real-time voice agent
AI Models| Conversation and intelligence
SQLite| Local database and memory
PyMuPDF| PDF processing
Pytest| Automated testing
Git & GitHub| Version control

---

📁 Project Structure

SanX Assistant/
│
├── agent.py
├── assistant_router.py
├── chat_engine.py
├── command_parser.py
├── commands.py
│
├── database.py
├── document_db.py
├── document_manager.py
├── document_processor.py
├── pdf_reader.py
│
├── progress.py
├── knowledge_base.py
├── task_manager.py
├── reminder.py
├── study.py
├── quiz.py
├── placement.py
│
├── desktop_control.py
├── file_operations.py
│
├── test_chat.py
├── test_commands.py
├── test_tasks.py
├── test_quiz.py
├── test_study.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md

---

⚙️ Installation

1. Clone the repository

git clone https://github.com/sanx-labs26/Sanx-Assistant.git
cd SanX-Assistant

2. Create a virtual environment

python -m venv venv

3. Activate the virtual environment

Windows PowerShell

venv\Scripts\Activate.ps1

4. Install dependencies

python -m pip install -r requirements.txt

5. Configure environment variables

Create a ".env.local" file in the project directory.

Add your required API keys and configuration.

Example:

API_KEY=your_api_key_here

«Never upload your real API keys to GitHub.»

---

▶️ Running SanX

Activate your virtual environment:

venv\Scripts\Activate.ps1

Then start SanX:

python agent.py console

SanX will start in console mode and allow you to interact with the assistant.

---

🧪 Testing

SanX uses pytest for automated testing.

Install pytest:

python -m pip install pytest

Check the installation:

python -m pytest --version

Run the SanX test suite:

python -m pytest

«"python -m pytest" runs the tests created for SanX Assistant.
Do not use "python -m test" for the SanX test suite, because that runs Python's built-in CPython tests.»

---

🔐 Security

SanX may require API keys for AI services.

For security:

- Never commit ".env.local"
- Never publish API keys
- Keep secrets in environment variables
- Use ".gitignore" to protect sensitive files

Example ".gitignore":

venv/
.env
.env.local
__pycache__/
*.pyc
*.db
.pytest_cache/

---

🎯 Project Goals

SanX Assistant was created to explore and build practical skills in:

- Python development
- AI assistants
- Voice AI
- Natural language processing
- SQLite databases
- Automation
- Software testing
- Git and GitHub
- AI-powered productivity tools

---

🚀 Version

SanX Assistant V1

Status: Release Candidate / V1

V1 focuses on creating a functional personal AI assistant with:

- Voice interaction
- AI conversation
- Study Mode
- Quiz Mode
- Placement Interview Mode
- Task Management
- Progress Tracking
- Memory
- PDF/document processing
- Desktop and file operations
- Automated testing

---

🔮 Future Plans

Possible future improvements include:

- Android application
- Better voice interaction
- More AI models
- Advanced long-term memory
- Improved desktop automation
- More study subjects
- Advanced placement preparation
- Improved document understanding
- Better user interface
- Performance improvements

---

📜 License

SanX Assistant V1 is released under the MIT License.

See the "LICENSE" file for the complete license text.

---

👨‍💻 Author

Santhosh

Built as a personal AI assistant and portfolio project while learning and developing skills in Data Science, Data Analytics, Python, AI, and software development.

---

⭐ Support

If you find SanX Assistant interesting, consider giving the repository a ⭐ on GitHub.

---

«SanX — Your AI assistant for learning, productivity, and preparation.»
