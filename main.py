import discord
from settings import *
from discord_components import ComponentsBot

#bot = commands.Bot(command_prefix="=")
bot = ComponentsBot(command_prefix="=", intents=discord.Intents().all())

@bot.event
async def on_ready():
    print('Logged on as {0}!'.format(bot.user))

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(DISCORD_BOT_TOKEN)