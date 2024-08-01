from langchain_community.tools.human.tool import HumanInputRun

from utils.console import ask


def human_console_input():
    return HumanInputRun(
        description="Ask for human help only when needed, try to do as little as possible",
        input_func=lambda: ask(prompt="📝"),
    )
