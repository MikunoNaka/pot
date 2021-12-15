import os
from dotenv import load_dotenv
import discord

from clients.pot import Pot

def main():
    # load env vars to get bot token
    load_dotenv('.env')

    intents = discord.Intents.default()
    intents.members = True

    bot = Pot(
        command_prefix=".",
        intents=intents
    )

    for file in os.listdir("./cogs/"):
        if file.endswith(".py"):
            bot.load_extension(f"cogs.{file[:-3]}")

    bot.run(os.getenv('BOT_TOKEN'))

if __name__ == "__main__":
    main()
