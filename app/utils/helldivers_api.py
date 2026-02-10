import aiohttp
import os
import json
from dotenv import load_dotenv

PLANETS_FILE = 'app/storage/planets.json'

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
                    raw_data = await response.json()
                    return raw_data['current']
        return self.cached_season # If the cache is not empty, return the cache.
            
    #This function will return the last given event message + title        
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
    
    #This function will return a list of worlds that are currently active
    async def current_status(self):
        season_id = await self.current_season() # Get the cached current season
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.api_url}/api/{season_id}/status") as response:
                raw_data = await response.json()
                index_list = []
                for campaign in raw_data['campaigns']:
                    index_list.append(campaign['planet']['index'])
                return index_list

    # Write a list of all planets to a json file
    async def all_planets(self):
        
        # If no planets.json file exists, create it
        if  not os.path.exists(PLANETS_FILE):
            # Create the file, return the data from the file
            season_id = await self.current_season() # Get the cached current season
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.api_url}/api/{season_id}/planets") as response:
                    raw_data = await response.json()

            # create json file with planets and ids
            planets = {planet['name']: planet['index'] for planet in raw_data}
            
            # write to file
            with open(PLANETS_FILE, 'w') as file:
                json.dump(planets, file)
        
        # Return the file data    
        with open(PLANETS_FILE, 'r') as data:
            return json.load(data)
    
    # Return the status of a specific planet        
    async def get_planet(self, planet_name="Super Earth"):
        season_id = await self.current_season() # Get the cached current season
        planet_id = await self.get_planet_id(planet_name)
        
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.api_url}/api/{season_id}/planets/{planet_id}/status") as response:
                data = await response.json()
                return data
            
    # Return the id of a specific planet
    async def get_planet_id(self, planet_name):
        planets = await self.all_planets()
        return planets[planet_name]
    
    
    