import requests
import time
from app.core.config import Config
from app.schemas.schema import SearchRequest, SearchResponse, SearchResult


class BraveSearchService:
    def search(self, search_request: SearchRequest) -> SearchResponse:
        start_time = time.time()
        
        payload = {
            "api_key": Config.API_KEY,
            "query": search_request.query,
            "max_results": search_request.count,
            "include_answer": True
        }
        
        response = requests.post(
            Config.TAVILY_BASE_URL,
            json=payload,
            timeout=Config.TIMEOUT
        )
        
        if response.status_code != 200:
            raise ValueError(f"API error: {response.status_code}")
        
        data = response.json()
        results = [
            SearchResult(
                title=r.get("title", ""),
                url=r.get("url", ""),
                description=r.get("content", ""),
                position=i + 1
            )
            for i, r in enumerate(data.get("results", []))
        ]
        
        search_time_ms = (time.time() - start_time) * 1000
        
        return SearchResponse(query=search_request.query, results=results, search_time_ms=search_time_ms)
