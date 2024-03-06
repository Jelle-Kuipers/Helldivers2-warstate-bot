from discord.ext import commands

# This is a cog, a class that contains commands
class HelloCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # This is a command, a function that can be called by a user    
    @commands.slash_command()
    async def hello(self, ctx, name: str = None):
        name = name or ctx.author.name
        await ctx.respond(f"Hello you {name}!")

# This function is called in app/slash_commands/__init__.py, and adds the command to the bot
def setup(bot):
    bot.add_cog(HelloCog(bot))
