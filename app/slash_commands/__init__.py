import os

# This function is called in app/main.py
def setup(bot):
    # Each file in the directory contains a command, that is loaded as a cog in the file
    for filename in os.listdir('./app/slash_commands'):
        if filename.endswith('.py') and filename != '__init__.py':
            bot.load_extension(f'slash_commands.{filename[:-3]}')
            print(f'Loaded slash command: {filename[:-3]}')