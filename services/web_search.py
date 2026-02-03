import requests
from mcp.core.config import Config
from schemas.schema import SearchRequest, SearchResponse, SearchResult


class BraveSearchService:
    def search(self, search_request: SearchRequest) -> SearchResponse:
        """Execute a web search using Brave Search API."""
        response = requests.get(
            f"{Config.BRAVE_SEARCH_BASE_URL}/web/search",
            headers=Config.get_brave_headers(),
            params={"q": search_request.query, "count": search_request.count},
            timeout=Config.REQUEST_TIMEOUT
        )
        
        if response.status_code != 200:
            raise Exception(f"Brave API error: {response.status_code}")
        
        data = response.json()
        results = [
            SearchResult(
                title=r.get("title", ""),
                url=r.get("url", ""),
                description=r.get("description", ""),
                position=i + 1
            )
            for i, r in enumerate(data.get("results", []))
        ]
        
        return SearchResponse(query=search_request.query, results=results)