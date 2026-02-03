from pydantic import BaseModel, Field
from typing import List
from datetime import datetime


class SearchRequest(BaseModel):
    query: str = Field(..., min_length=1)
    count: int = Field(default=10, ge=1, le=20)


class SearchResult(BaseModel):
    title: str
    url: str
    description: str
    position: int


class SearchResponse(BaseModel):
    query: str
    results: List[SearchResult] = Field(default_factory=list)
    search_time_ms: float = 0
    timestamp: datetime = Field(default_factory=datetime.utcnow)
