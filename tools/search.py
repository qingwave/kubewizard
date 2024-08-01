from langchain_community.tools.ddg_search.tool import DuckDuckGoSearchRun, DuckDuckGoSearchResults
from langchain_community.utilities.duckduckgo_search import DuckDuckGoSearchAPIWrapper

def create_search_tool():
    return DuckDuckGoSearchResults(
        description="""
        Search the web for information on a topic, there are some useful websites for k8s info:
        - https://kubernetes.io/docs/: Official Kubernetes documentation
        - https://kuberentes.io: Kubernetes community site
        - https://github.com/kubernetes/kubernetes: Kubernetes GitHub repository
        """,
        api_wrapper=DuckDuckGoSearchAPIWrapper(
            max_results=10,
            time="y",
            backend="api",
            source="text"
        )
    )

if __name__ == "__main__":
    tool = create_search_tool()
    tool.run("k8s latest version", verbose=True)
