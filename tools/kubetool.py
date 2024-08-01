from typing import Optional, Type, Any, Callable

from langchain_core.pydantic_v1 import Field, BaseModel
from langchain_core.callbacks import CallbackManagerForToolRun
from langchain_community.tools.shell.tool import ShellTool

from utils.console import confirm

def _default_approve(_input: str) -> bool:
    msg = "Do you approve of the following input? "
    return confirm(msg, extra=_input)

class KubeInput(BaseModel):
    """Args for the k8s tool."""

    commands: str = Field(
        ...,
        example="kubectl get pods",
        description="The kubectl/helm related command to run.",
    )
    """ Kubectl commands to run."""

class KubeTool(ShellTool):
    name = "KubeTool"
    """Name of tool."""

    description = "Tool to run k8s related commands(kubectl, helm) on the Kubernetes cluster. The input is the string command to run."
    """Description of tool."""

    args_schema: Type[BaseModel] = KubeInput
    
    def _run(
        self,
        commands: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Run commands and return final output."""
        commands = self._parse_commands(commands)
        return super()._run(commands)

    def _parse_commands(self, commands: str) -> str:
        """Parse commands."""
        return commands.strip().strip('"`')

class KubeToolWithApprove(KubeTool):
    """Tool to run k8s related commands and check if need approve for the commands."""

    name = "KubeToolWithApprove"
    """Name of tool."""

    approve: Callable[[Any], bool] = _default_approve

    description = "Tool to run k8s related commands and with approve check, if command will modify resource(delete, patch, create, update and so on) or view credential info(secret) need approve. args: type string, the raw string of command."
    """Description of tool."""

    args_schema: Type[BaseModel] = KubeInput

    def _run(
        self,
        commands: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Run commands and return final output."""
        if not self.approve(commands):
            return "Command execution aborted by user, not approved."

        return super()._run(commands)
