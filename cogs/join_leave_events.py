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

# import ../config.py
try: 
   from config import WELCOME_CHANNEL_ID, GOODBYE_CHANNEL_ID
except ImportError:
    WELCOME_CHANNEL_ID = None
    GOODBYE_CHANNEL_ID = None

class JoinLeaveEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        message = WELCOME_MESSAGE.format(username=member)

        # check which channel to send to
        if WELCOME_CHANNEL_ID != None:
            channel = self.bot.get_channel(WELCOME_CHANNEL_ID)
        elif member.guild.system_channel:
            channel = member.guild.system_channel
        else:
            return

        await channel.send(message)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        message = GOODBYE_MESSAGE.format(username=member)

        # check which channel to send to
        if WELCOME_CHANNEL_ID != None:
            channel = self.bot.get_channel(WELCOME_CHANNEL_ID)
        elif member.guild.system_channel:
            channel = member.guild.system_channel
        else:
            return

        await channel.send(message)

def setup(bot):
    bot.add_cog(JoinLeaveEvents(bot))
