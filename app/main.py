import discord
import dotenv
import os

# load env
dotenv.load_dotenv()
TOKEN = str(os.getenv("TOKEN"))
STATUS = int(os.getenv("STATUS"))

# create bot
bot = discord.Bot()

# hello slash command
@bot.slash_command()
async def hello(ctx, name: str = None):
    name = name or ctx.author.name
    await ctx.respond(f"Hello you {name}!")
    
# bot is online
@bot.event
async def on_ready():
    channel = bot.get_channel(STATUS)
    await channel.send("Bot is online!")

bot.run(TOKEN)