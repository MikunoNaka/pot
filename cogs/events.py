# Pot - Discord bot which is pog. Pot.
# Version - 0.1
# Licensed under the MIT license - https://opensource.org/licenses/MIT
#
# Copyright (c) 2021 Vidhu Kant Sharma

import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # only works for my server
        channel = self.bot.get_channel(920729804129587301)
        await channel.send(f"{member} has joined our server.")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        # only works for my server
        channel = self.bot.get_channel(920729740611039252)
        await channel.send(f"{member} has left our server.")

def setup(bot):
    bot.add_cog(Events(bot))
