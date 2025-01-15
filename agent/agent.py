import os
from typing import Optional
from langchain_core.prompts import PromptTemplate
from langchain.agents import create_react_agent, AgentExecutor
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from langchain_core.language_models.chat_models import BaseChatModel

from .prompt import REACT_PROMPT
from tools import *

class KubeAgent:
    """KubeAgent is an AI agent that helps users with Kubernetes issues.

    Init args — completion params:
    - llm: llm model
    - debug_level: debug level for the agent, 0 is no debug, 1 is verbose, 2 is verbose with intermediate steps
    """

    name: str = "KubeAgent"

    tools = [KubeTool(), KubeToolWithApprove(), human_console_input(), create_search_tool(), RequestsGet(allow_dangerous_requests=True)]

    prompt = PromptTemplate.from_template(REACT_PROMPT, tools=tools)

    def __init__(self, llm: BaseChatModel= ChatOpenAI(model="gpt-4o-mini", temperature=0.7), debug_level: Optional[int] = None):
        self.memory = ConversationBufferMemory(memory_key="chat_history")

        agent = create_react_agent(llm, self.tools, self.prompt)

        verbose = False
        return_intermediate_steps = False
        if debug_level is None:
            debug_level = int(os.getenv("DEBUG_LEVEL", "1"))

        if debug_level == 1:
            verbose = True
        elif debug_level >= 2:
            verbose = True
            return_intermediate_steps = True

        self.agent = AgentExecutor(
            name=self.name,
            agent=agent,
            memory=self.memory,
            tools=self.tools,
            return_intermediate_steps=return_intermediate_steps,
            handle_parsing_errors=True,
            verbose=verbose,
        )

    def invoke(self, input: str):
        return self.agent.invoke({
            "input": input,
            "chat_history": self.get_chat_messages(),
        })

    def get_chat_messages(self):
        return self.memory.chat_memory.messages
