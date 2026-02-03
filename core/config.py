import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_KEY = os.getenv("API_KEY", "")

    
    @staticmethod
    def get_headers():
        return {
            "Authorization": f"Bearer {Config.API_KEY}",
            "Accept": "application/json",
        }
