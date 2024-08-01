from rich.prompt import Prompt
from rich.prompt import Confirm
from rich.style import Style, Color

class PyPrompt(Prompt):
    def __init__(self, *args, suffix: str="> ", **kwargs):
        super().__init__(*args,  **kwargs)
        self.prompt_suffix = suffix

def ask(prompt: str, color: str="bold cyan") -> str:
    prompt = f"[{color}]{prompt}[/{color}]"
    line = PyPrompt.ask(prompt=prompt, show_default=False)
    return line

def confirm(msg: str, extra: str = "") -> bool:
    if extra:
        msg = f"✅ {msg}\n[cyan]{extra}[/cyan]"
    resp = Confirm.ask(msg, default=False)
    if isinstance(resp, bool):
        return resp
    elif resp.lower() == "y" or resp.lower() == "yes":
        return True
    return resp
