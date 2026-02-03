import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_KEY = os.getenv("API_KEY", "")
    TAVILY_BASE_URL = os.getenv("TAVILY_BASE_URL", "")
    TIMEOUT = 10
    
    @staticmethod
    def get_headers():
        return {
            "Content-Type": "application/json",
        }
