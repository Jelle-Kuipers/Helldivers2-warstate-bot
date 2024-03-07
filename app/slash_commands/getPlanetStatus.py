from discord.ext import commands
import discord
from utils.helldivers_api import Helldivers_Api
import json
from datetime import datetime

# This is a cog, a class that contains commands
class planetStatusCommandCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.helldivers_api = Helldivers_Api()
    
    def autocomplete(ctx):
        with open('app/storage/planets.json') as file:
            planets = json.load(file).keys()
            return [planet for planet in planets if planet.startswith(ctx.value)]
    
    # This is a command, a function that can be called by a user    
    @commands.slash_command(description="Get the status of a planet.")
    async def status(self, ctx, name : discord.Option(str, description="The name of the planet you'd like a report for", required=True, autocomplete=autocomplete)):     # type: ignore #this is actually valid and working
        # Get the planet status from the API
        planet_status = await self.helldivers_api.get_planet(name)
        
        # Make the liberation progress a percentage, generate a report date and format the player count
        liberation_progress = round(planet_status["liberation"], 2)
        report_date = datetime.now().strftime("%Y-%m-%d")
        player_count = planet_status["players"]
        if player_count > 1000:
            player_count = round(planet_status["players"] / 1000)
            player_count = f"{player_count}k"
        elif player_count == 0:
            player_count = "0"
        
        if liberation_progress.is_integer():
            liberation_progress = int(liberation_progress)
                
        # Based on the owner of the planet, set the colour and thumbnail of the embed
        if planet_status["owner"] == "Humans":
            colour = discord.Colour.light_grey()
            thumbnail_url = "https://i.ibb.co/JQZ3DDQ/Super-earth.webp"
        elif planet_status["owner"] == "Terminids":
            colour = discord.Colour.dark_gold()
            thumbnail_url = "https://i.ibb.co/HB48wTC/Terminidlogo.webp"
        else: # Automatons
            colour = discord.Colour.red()
            thumbnail_url = "https://i.ibb.co/2qVThTT/Automatonlogo.webp"
        
        # Create the embed
        embed = discord.Embed(
            title="Planet status report:",
            color=colour
        )
        embed.add_field(name="Name", value=planet_status["planet"]["name"], inline=False)
        # embed.add_field(name="Sector", value=planet_status["planet"]["sector"], inline=False) # This is currently disabled as the API only returns some names.
        
        embed.add_field(name="Occupied by", value=planet_status["owner"], inline=True)
        embed.add_field(name="Liberation progress", value=f"{liberation_progress}%", inline=True)

        embed.add_field(name="Number of active helldivers", value=player_count, inline=False)
        
        embed.set_author(name=f"Ministry of defence | Report generated on {report_date}", icon_url="https://i.ibb.co/JQZ3DDQ/Super-earth.webp")
        
        embed.set_thumbnail(url=thumbnail_url)
        
        # Send the embed
        await ctx.respond(embed=embed)

# This function is called in app/slash_commands/__init__.py, and adds the command to the bot
def setup(bot):
    bot.add_cog(planetStatusCommandCog(bot))
