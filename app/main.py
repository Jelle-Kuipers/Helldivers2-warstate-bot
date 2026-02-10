import discord
import dotenv
import os
import datetime

# load env vars
dotenv.load_dotenv()
TOKEN = str(os.getenv("TOKEN"))
STATUS = int(os.getenv("STATUS"))

# create a bot instance
bot = discord.Bot()
    
# Load the "modules" by specifying their directory names    
modules = ['slash_commands']
for module in modules:
    bot.load_extension(f'{module}')
    
# Once the bot is ready, send a message to the given status channel
@bot.event
async def on_ready():
    channel = bot.get_channel(STATUS)
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    await channel.send(f"Bot is online! Current time is {current_time}")

# Start the bot
bot.run(TOKEN)