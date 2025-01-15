from typing import Any
from langchain_community.tools.requests.tool import RequestsGetTool
from langchain_community.utilities.requests import TextRequestsWrapper
from bs4 import BeautifulSoup
from html2text import HTML2Text

def get_parser() -> HTML2Text:
    parser: HTML2Text = HTML2Text()
    parser.ignore_links = True
    parser.ignore_images = True
    parser.ignore_emphasis = True
    parser.ignore_mailto_links = True
    return parser

class RequestsGet(RequestsGetTool):
    name: str = "RequestsGet"
    description: str = """A portal to the internet. Use this when you need to get specific
    content from a website. Input should be a url (i.e. https://www.kubernetes.io/releases).
    The output will be the text response of the GET request.
    """
    requests_wrapper: str = TextRequestsWrapper()
    allow_dangerous_requests: bool = True

    parser: HTML2Text = get_parser()

    def _run(self, url: str, **kwargs: Any) -> str:
        url = url.strip().strip('"`')
        response = super()._run(url, **kwargs)
        soup = BeautifulSoup(response, 'html.parser')
        for tag in soup(['header', 'footer', 'script', 'styple']):
            tag.decompose()
        data = self.parser.handle(soup.prettify())
        return data

if __name__ == "__main__":
    tool = RequestsGet(allow_dangerous_requests=True)
    print(tool.invoke("https://www.kubernetes.io/releases"))
