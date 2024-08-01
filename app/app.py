import readline
import time
import signal
from typing import Callable, Dict, List, Optional, Any
from rich.console import Console
from rich.prompt import Prompt
from pyfiglet import figlet_format

# Define the type for command handlers
CommandHandler = Callable[[Console, str], None]

class Handler:
    def __init__(self, name: str, handler: CommandHandler, description: str):
        self.name = name
        self.handler = handler
        self.description = description

class ConsoleApp:
    def __init__(
        self,
        name: str,
        description: str,
        command_handlers: Optional[List[Handler]] = None,
        default_handler: Optional[Handler] = None,
    ):
        """
        Initialize the console application.

        :param name: The application name.
        :param description: The application description.
        :param command_handlers: List of handlers for commands.
        :param default_handler: Default handler for unknown commands.
        """
        self.name = name
        self.description = description
        self.console = Console()
        self.command_handlers: Dict[str, Handler] = {handler.name: handler for handler in (command_handlers or [])}
        self.default_handler = default_handler or Handler("default", self.unknown_command_handler, "Default handler.")
        self.ctrl_c_count = 0

        # Register default handlers
        self.register_default_handlers()

    def register_default_handlers(self):
        """
        Register default command handlers.
        """
        self.command_handlers.setdefault("help", Handler("help", self.help_handler, "Print help info."))
        self.command_handlers.setdefault("exit", Handler("exit", self.exit_handler, "Exit the application."))
        self.command_handlers.setdefault("clear", Handler("clear", self.clear_handler, "Clear the screen."))

    def handle_interrupt(self, sig: int, frame: Any):
        """
        Handle Ctrl+C to provide a graceful exit.

        :param sig: Signal number.
        :param frame: Current stack frame.
        """
        self.ctrl_c_count += 1
        if self.ctrl_c_count == 1:
            self.console.print("Press Ctrl+C again to exit", style="red bold")
            time.sleep(0.5)
        elif self.ctrl_c_count >= 2:
            self.console.print("Goodbye!", style="cyan bold")
            exit(0)

    def print_welcome_message(self):
        """
        Print the welcome message and application title in ASCII art.
        """
        self.console.print(f"🎉 Welcome to {self.name}!")
        self.console.print(self.description, highlight=False)
        self.console.print("Type 'help' to see available commands.", highlight=False)
        self.console.print(figlet_format(self.name), style="cyan bold", highlight=False)

    def execute_command(self, command: str, raw: str):
        """
        Execute the given command.

        :param command: Command to execute.
        :param raw: Raw command input.
        """
        self.ctrl_c_count = 0
        handler = self.command_handlers.get(command, self.default_handler).handler
        handler(self.console, raw)

    def run(self):
        """
        Start the application and enter the command loop.
        """
        signal.signal(signal.SIGINT, self.handle_interrupt)
        self.print_welcome_message()

        while True:
            try:
                user_input = Prompt.ask(f"[magenta]{self.name.lower()}>[/magenta]")
                if user_input:
                    readline.add_history(user_input)

                command_parts = user_input.strip().lower().split()
                if not command_parts:
                    self.console.print("")
                    continue
                command = command_parts[0]
                self.execute_command(command, user_input)
            except EOFError:
                self.console.print("Exiting...", style="red bold")
                break

    def help_handler(self, console: Console, args: Any):
        """
        Display a list of available commands.

        :param console: Console instance for printing.
        :param args: Additional arguments (unused).
        """
        console.print("Available commands:", style="blue bold")
        max_width = max(len(handler.name) for handler in self.command_handlers.values())
        for handler in self.command_handlers.values():
            console.print(f"  - {handler.name.ljust(max_width)}:  {handler.description}", style="blue")
        
        default_name = "*"
        console.print(f"  - {default_name.ljust(max_width)}:  {self.default_handler.description}", style="blue")

    def clear_handler(self, console: Console, args: Any):
        """
        Clear the screen.

        :param console: Console instance for printing.
        :param args: Additional arguments (unused).
        """
        console.clear()

    def exit_handler(self, console: Console, args: Any):
        """
        Exit the application.

        :param console: Console instance for printing.
        :param args: Additional arguments (unused).
        """
        console.print("Goodbye!", style="cyan bold")
        exit(0)

    def unknown_command_handler(self, console: Console, args: Any):
        """
        Handle unknown commands.

        :param console: Console instance for printing.
        :param args: Additional arguments (unused).
        """
        console.print("Unknown command. Type 'help' for a list of available commands.", style="red bold")

# Example usage
if __name__ == "__main__":
    app = ConsoleApp(
        "DemoApp",
        "This is a demo app.",
        command_handlers=[
            Handler("echo", lambda console, args: console.print(f"Echo: [blue]{args}[/blue]"), "Echo the input."),
        ],
    )
    app.run()
