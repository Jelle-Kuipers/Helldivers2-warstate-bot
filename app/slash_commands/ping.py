from discord.ext import commands

# This is a cog, a class that contains commands
class pingCommandCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # This is a command, a function that can be called by a user    
    @commands.slash_command(description="Sends the bot's latency.")
    async def ping(self, ctx):
        await ctx.respond(f"Received. Latency is **{round(self.bot.latency * 1000)}ms**")

# This function is called in app/slash_commands/__init__.py, and adds the command to the bot
def setup(bot):
    bot.add_cog(pingCommandCog(bot))
