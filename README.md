# 🤖 SanX Assistant

An AI-powered desktop assistant built with Python that provides intelligent conversations, remembers user interactions using SQLite, and is designed with a modular architecture for future expansion.

---

## 📖 Overview

SanX Assistant is a personal AI assistant that combines conversational AI with persistent memory. It stores conversation history and user preferences in a SQLite database, allowing the assistant to remember information across sessions.

This project demonstrates Python programming, database integration, Git/GitHub workflow, and software engineering best practices.

---

## ✨ Features

- 💬 AI-powered conversational assistant
- 🧠 SQLite-based memory storage
- 📝 Stores conversation history
- ⚙️ User preference management
- 🗄️ Persistent database using SQLite
- 🛡️ Robust error handling with `try-except`
- 📂 Modular Python project structure
- 🔄 Easy to extend with new features

---

## 📅 Week 3 Progress

During Week 3, the following features were completed:

- ✅ SQLite database integration
- ✅ Memory storage implementation
- ✅ Conversation history management
- ✅ User preferences storage
- ✅ Database read and write operations
- ✅ Error handling improvements
- ✅ Git and GitHub integration
- ✅ Project structure organization

---

## 🛠️ Technologies Used

- Python 3
- SQLite
- Git
- GitHub

---

## 📂 Project Structure

```
SanX Assistant/
│── database.py
│── read_db.py
│── sanx.db
│── README.md
│── requirements.txt
```

---

## 🗄️ Database

The assistant uses **SQLite** (`sanx.db`) for persistent storage.

### Tables

**conversations**
- Stores chat history
- Saves user messages
- Saves assistant responses

**preferences**
- Stores user preferences
- Maintains personalized settings

---

## 🛡️ Error Handling

The application includes:

- Database connection error handling
- Safe database operations
- Exception handling using `try-except`
- Input validation
- Graceful failure handling

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/SanX-Assistant.git
```

### Move into the project directory

```bash
cd SanX-Assistant
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python main.py
```

> Replace `main.py` with your project's actual entry file if it has a different name.

---

## 📸 Screenshots

Add screenshots of your application here.

Example:

```
images/home.png
images/chat.png
```

---

## 🔮 Future Enhancements

- Voice commands
- Text-to-Speech
- Speech Recognition
- Wake-word detection
- GUI interface
- Cloud database support
- Web search integration
- Calendar and reminder support

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Santhosh M**

GitHub: https://github.com/sanx-labs26

---

⭐ If you like this project, please consider giving it a **Star** on GitHub!

