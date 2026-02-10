from discord.ext import commands
import discord
from utils.helldivers_api import Helldivers_Api

# This is a cog, a class that contains commands
class ordersCommandCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.helldivers_api = Helldivers_Api()
    
    # This is a command, a function that can be called by a user    
    @commands.slash_command(description="Get the latest issued orders from Super Earth")
    async def orders(self, ctx):
        current_season = await self.helldivers_api.current_event()
        embed = discord.Embed(
            title="Incoming message",
            color=discord.Colour.light_grey()
        )
        embed.add_field(name=current_season["title"], value=current_season["message"], inline=False)
        embed.set_author(name="Ministry of defence")
        embed.set_thumbnail(url="https://i.ibb.co/JQZ3DDQ/Super-earth.webp")
        
        await ctx.respond(embed=embed)

# This function is called in app/slash_commands/__init__.py, and adds the command to the bot
def setup(bot):
    bot.add_cog(ordersCommandCog(bot))
