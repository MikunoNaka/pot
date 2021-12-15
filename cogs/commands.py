# Pot - Discord bot which is pog. Pot.
# Version - 0.1
# Licensed under the MIT license - https://opensource.org/licenses/MIT
#
# Copyright (c) 2021 Vidhu Kant Sharma

import discord
from discord.ext import commands

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pepe(self, ctx):
        await ctx.send("pepe")

    @commands.command()
    async def context(self, ctx):
        print(ctx.__dict__)

def setup(bot):
    bot.add_cog(Commands(bot))
