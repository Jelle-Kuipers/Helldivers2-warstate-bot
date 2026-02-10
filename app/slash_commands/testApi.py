from discord.ext import commands
import aiohttp

# This is a cog, a class that contains commands
class TestApiCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # This is a command, a function that can be called by a user    
    @commands.slash_command()
    async def TestApi(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get('http://helldivers2:4000/api') as response:
                await ctx.respond(response)

# This function is called in app/slash_commands/__init__.py, and adds the command to the bot
def setup(bot):
    bot.add_cog(TestApiCog(bot))
