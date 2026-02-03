from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


# search shema
class SearchRequest(BaseModel):
    query: str = Field(
        ..., min_length=1, max_length=2000, description="Search query string"
    )
    count: int = Field(
        default=10, ge=1, le=20, description="Number of results to return"
    )
    offset: int = Field(default=0, ge=0, description="Result offset for pagination")


# search result schema
class SearchResult(BaseModel):
    title: str = Field(..., description="Result title")
    url: str = Field(..., description="Result URL")
    description: str = Field(default="", description="Result snippet/description")
    position: int = Field(..., description="Result position in the list")


# search response schema
class SearchResponse(BaseModel):
    query: str = Field(..., description="Original search query")
    results: List[SearchResult] = Field(
        default_factory=list, description="List of search results"
    )
    total_results: int = Field(
        default=0, description="Total number of results available"
    )
    search_time_ms: float = Field(
        default=0, description="Time taken to search in milliseconds"
    )
    timestamp: datetime = Field(
        default_factory=datetime.utcnow, description="Response timestamp"
    )
