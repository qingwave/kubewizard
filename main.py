import dotenv

from agent import KubeAgent
from app import ConsoleApp, Handler


def main():
    dotenv.load_dotenv()

    kube_agent = KubeAgent()

    app = ConsoleApp(
        "KubeWizard",
        "This an AI agent for kubernetes, it can troubling shooting, deploy, and manage kubernetes.",
        command_handlers=[
            Handler(
                "clear",
                lambda console, args: console.clear(),
                "Clear the chat history.",
            ),
            Handler(
                "history",
                lambda console, args: console.print(kube_agent.get_chat_messages()),
                "Display the chat history.",
            ),
        ],
        default_handler=Handler(
            "default",
            lambda console, args: kube_agent.invoke(args),
            "Ask me everything about your kubernetes cluster(why my nginx pod not ready)",
        ),
    )

    app.run()


if __name__ == "__main__":
    main()
