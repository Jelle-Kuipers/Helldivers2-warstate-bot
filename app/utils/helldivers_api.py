import aiohttp
import os
from dotenv import load_dotenv

class Helldivers_Api:
    def __init__(self):
        load_dotenv()  # Load environment variables from .env file
        self.api_url = os.getenv('API_URL')
        self.cached_season = None # Cache the current season
        
    #This function will fill the cache if empty, otherwise it'll return the cache.
    async def current_season(self):
        if self.cached_season is None: # If the cache is empty, make the call to fill cache.
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.api_url}/api") as response:
                    data = await response.json()
                    return data['current']
        return self.cached_season # If the cache is not empty, return the cache.
            
    async def current_event(self):
        season_id = await self.current_season() # Get the cached current season
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.api_url}/api/{season_id}/events/latest") as response:
                raw_data = await response.json()
                # The API returns a lot of data, we only need the title and the message in English
                data = {
                    "title": raw_data["title"],
                    "message": raw_data["message"]["en"]
                }
                return data
