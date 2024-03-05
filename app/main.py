import discord
import os
from dotenv import load_dotenv

#load ENV
load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()

client = discord.Client(intents=intents)

#Once online, run
@client.event
async def on_ready():
    print(f'Started {client.user}')
    channel = client.get_channel(1157636928527671387)
    await channel.send('Systems starting...')
    
client.run(TOKEN)