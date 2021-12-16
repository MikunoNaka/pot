# Pot - Discord bot which is pog. Pot.
# Version - 0.1
# Licensed under the MIT license - https://opensource.org/licenses/MIT
#
# Copyright (c) 2021 Vidhu Kant Sharma

import discord
from discord.ext import commands

# to import from parent directory
import sys
sys.path.append('..')

# import ../phrases.py
try: 
   from phrases import WELCOME_MESSAGE, GOODBYE_MESSAGE
except ImportError:
    WELCOME_MESSAGE = "{username} has joined our server."
    GOODBYE_MESSAGE = "{username} has left our server."

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # only works for my server
        channel = self.bot.get_channel(920729804129587301)
        await channel.send(WELCOME_MESSAGE.format(username=member))

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        # only works for my server
        channel = self.bot.get_channel(920729740611039252)
        await channel.send(GOODBYE_MESSAGE.format(username=member))

def setup(bot):
    bot.add_cog(Events(bot))
