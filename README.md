# ✨ StudySpark

### Your local study buddy for learning, coding, and curious questions.

StudySpark is a lightweight command-line AI tutor powered by [Ollama](https://ollama.com/) and the Qwen model. Ask it to explain a tricky idea, quiz you one question at a time, or help you understand a piece of code—all using a model running on your own computer.

> Learn at your pace. Practice one question at a time. Keep your notes close.

## What it can do

- **Explain topics** in plain language, with examples and analogies.
- **Quiz you** one question at a time, then give feedback on your answer.
- **Help you learn programming**, explain code, debug snippets, and create practice exercises.
- **Save and recall study notes** between sessions.
- **Calculate basic arithmetic** and tell you the current date and time.

## Quick start

### 1. Install Ollama and get the model

Install [Ollama](https://ollama.com/), then download the model:

```bash
ollama pull qwen3.5:4b
```

Make sure Ollama is running before starting StudySpark.

### 2. Set up the project

You’ll need Python 3.10 or newer. From the project folder, create and activate a virtual environment, then install the dependency:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows PowerShell, activate the environment with:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Start learning

```bash
python agent.py
```

Type `quit` or `exit` to leave.

## Give it a try

```text
Explain fractions like I'm new to them.
Quiz me on the water cycle, one question at a time.
Teach me Python variables with a small example.
Give me a beginner Python exercise about loops, but don't show the answer yet.
Can you explain this code and help me find the bug?
Save photosynthesis as a topic I want to review.
Show me my saved study topics.
```

For programming help, mention the language you’re learning (for example, Python or JavaScript) and your experience level. StudySpark can then tailor its explanations and exercises.

## Notes and privacy

StudySpark connects to Ollama at `http://localhost:11434/v1` and uses the local `qwen3.5:4b` model. Study notes are stored in `notes.txt` beside the script. That file is ignored by Git so your personal notes aren’t included when you publish the project.

## Project files

```text
agent.py        The StudySpark assistant
requirements.txt Python dependencies
notes.txt       Your local study notes (created when you save a note)
```

## Troubleshooting

- **Model not found:** run `ollama pull qwen3.5:4b`.
- **Can’t connect:** make sure Ollama is running, then check the model with `ollama list`.
- **Python dependency missing:** activate your virtual environment and run `python -m pip install -r requirements.txt`.

---

Made for learning, experimenting, and building your first local AI project. 🌱
