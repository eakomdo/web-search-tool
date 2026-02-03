import requests
import time
from app.core.config import Config
from schemas.schema import SearchRequest, SearchResponse, SearchResult


class BraveSearchService:
    def search(self, search_request: SearchRequest) -> SearchResponse:
        start_time = time.time()
        
        response = requests.get(
            f"{Config.BRAVE_BASE_URL}/web/search",
            headers=Config.get_headers(),
            params={"q": search_request.query, "count": search_request.count},
            timeout=Config.TIMEOUT
        )
        
        if response.status_code != 200:
            raise Exception(f"API error: {response.status_code}")
        
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
        
        search_time_ms = (time.time() - start_time) * 1000
        
        return SearchResponse(query=search_request.query, results=results, search_time_ms=search_time_ms)
