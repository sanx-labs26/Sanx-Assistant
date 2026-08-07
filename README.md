🚀 SanX Assistant

SanX Assistant is an AI-powered desktop voice assistant developed using Python and LiveKit. It enables natural voice interactions, study support, task management, file operations, and desktop automation, serving as a comprehensive productivity and learning companion.

---

✨ Features

- 🎙️ Real-time AI voice interaction
- 📚 Study Mode for structured learning
- 📝 Quiz Mode for knowledge assessment
- 💼 Placement Interview Preparation Mode
- ✅ Task Management (Add, View, Complete, Delete)
- 🧠 Knowledge Base with persistent memory
- 📂 File Search and File Access capabilities
- 💻 Desktop Automation support
- ⚡ Pre-processing of local commands before AI response
- 🗂️ SQLite-based persistent data storage
- 🔊 Enhanced high-quality speech output
- 🛡️ Robust error handling and modular design

---

🛠️ Tech Stack

- Python 3.11+
- LiveKit Agents
- Google Gemini API
- SQLite
- Asyncio
- Python Dotenv

---

📁 Project Structure

SanX-Assistant/
│
├── agent.py
├── database.py
├── task_manager.py
├── study.py
├── assistant_router.py
├── knowledge_base.py
├── progress.py
├── desktop_control.py
├── file_operations.py
├── reminder.py
├── config.py
├── requirements.txt
├── sanx.db
└── README.md

---

⚙️ Installation

git clone https://github.com/sanx-labs26/SanX-Assistant.git
cd SanX-Assistant

Create a virtual environment:

python -m venv venv

Activate it.

Windows

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Create a ".env" file and configure your API keys.

Run the assistant:

python agent.py console

---

🎯 Available Commands

Study

- Study Python
- Study Machine Learning
- Quiz Python

Tasks

- Add a task
- Show my tasks
- Complete task
- Delete task

Desktop

- Open Notepad
- Open Calculator
- Open Chrome
- Open Paint
- Open Explorer

Files

- Open filename
- Search filename
- Show files

---

🗄️ Database

SanX Assistant utilizes SQLite for persistent storage of:

- User preferences
- Tasks
- Knowledge base entries
- Conversation history
- Learning progress

---

🔮 Roadmap

Version 1 ✅

- Voice Assistant
- Study Mode
- Quiz Mode
- Placement Interview Mode
- Task Manager
- Knowledge Base
- Desktop Automation
- File Operations

Version 2 🚀

- Long-term memory system
- Calendar integration
- Email support
- Weather updates
- AI Vision capabilities
- OCR functionality
- Android companion application
- Advanced smart automation

---

🤝 Contributing

Contributions, suggestions, and bug reports are highly appreciated.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Submit a Pull Request

---

📄 License

This project is licensed under the MIT License.

---

👨‍💻 Developer

Santhosh M

B.Sc. Data Science and Data Analytics

Passionate about Artificial Intelligence, Voice Assistants, and Software Development.

GitHub: "https://github.com/sanx-labs26" (https://github.com/sanx-labs26)

---

⭐ Support

If you find this project useful, please consider giving it a ⭐ Star on GitHub. It helps increase visibility and supports continued development.

---

Built with ❤️ using Python, LiveKit, and AI.
