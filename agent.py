import ast
import operator
from datetime import datetime
from pathlib import Path

from pydantic_ai import Agent
from pydantic_ai.models.ollama import OllamaModel
from pydantic_ai.providers.ollama import OllamaProvider


MODEL_NAME = "qwen3.5:4b"
AGENT_NAME = "StudySpark"
NOTES_FILE = Path(__file__).with_name("notes.txt")

model = OllamaModel(
    MODEL_NAME,
    provider=OllamaProvider(base_url="http://localhost:11434/v1"),
)


def get_current_time() -> str:
    """Get the current date and time."""
    return datetime.now().strftime("%A, %B %d, %Y at %I:%M %p")


def calculate(expression: str) -> str:
    """Evaluate a basic math expression, e.g. '23 * 7 + 1'."""
    operations = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.UAdd: operator.pos,
        ast.USub: operator.neg,
    }

    def evaluate(node: ast.AST) -> int | float:
        if isinstance(node, ast.Expression):
            return evaluate(node.body)
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in operations:
            return operations[type(node.op)](evaluate(node.left), evaluate(node.right))
        if isinstance(node, ast.UnaryOp) and type(node.op) in operations:
            return operations[type(node.op)](evaluate(node.operand))
        raise ValueError("Use numbers and +, -, *, /, and parentheses only.")

    try:
        return str(evaluate(ast.parse(expression, mode="eval")))
    except (SyntaxError, ValueError, ZeroDivisionError, OverflowError) as error:
        return f"Error: {error}"


def save_note(note: str) -> str:
    """Save a short note so it can be recalled later."""
    with NOTES_FILE.open("a", encoding="utf-8") as file:
        file.write(f"- {note}\n")
    return "Note saved."


def read_notes() -> str:
    """Read back all previously saved notes."""
    if not NOTES_FILE.exists():
        return "No notes saved yet."
    with NOTES_FILE.open(encoding="utf-8") as file:
        return file.read()


agent = Agent(
    model,
    tools=[get_current_time, calculate, save_note, read_notes],
    instructions=(
        "You are a friendly study buddy running locally. Help the student learn, "
        "not just get answers. Explain difficult ideas in plain language and use "
        "short examples or analogies when helpful. You can teach programming in "
        "languages such as Python and JavaScript: explain code step by step, help "
        "debug code the student shares, and create small practice exercises. If "
        "the programming language or the student's experience level is unclear, "
        "ask before choosing one. When asked to quiz the student, "
        "ask one question at a time and wait for their answer. When they answer, "
        "say what they got right, gently correct mistakes, and explain why. Do not "
        "reveal a quiz answer before the student tries unless they ask. If a student "
        "says a topic is difficult or asks to remember it, offer to save a short "
        "study note; save it when they agree or explicitly ask, and only say it was "
        "saved after using the save-note tool. Use the notes tool to recall saved "
        "topics when asked. You can also help with basic arithmetic and the current "
        "time. Keep answers encouraging and concise."
    ),
)


def main() -> None:
    print(
        f"{AGENT_NAME} ready! Ask for an explanation, a quiz, programming help, "
        "or to review a saved topic.\n"
        "Type 'quit' or 'exit' to stop.\n"
    )
    history = []
    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if user_input.lower() in ("quit", "exit"):
            break
        if not user_input:
            continue

        result = agent.run_sync(user_input, message_history=history)
        history = result.all_messages()
        print(f"\nAgent: {result.output}\n")


if __name__ == "__main__":
    main()