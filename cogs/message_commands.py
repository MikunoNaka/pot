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
    from phrases import CLEAR
except ImportError:
    CLEAR = {
        "MissingPermissions": "You don't have the permissions to manage messages in this channel."
        , "ValueError": "Invalid arguments. Please specify number or messages (or leave blank to clear whole channel)"
    }

class MessageCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # clearing messages from current channel
    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def clear(self, ctx, *, amount=None):
        if amount:
            try:
                # deletes amount + 1 messages 
                # so user doesn't have to count the command itself
                await ctx.channel.purge(limit=int(amount)+1)
            except ValueError:
                # if invalid arguments (i.e string) are provided
                await ctx.send(CLEAR["ValueError"])
        else:
            await ctx.channel.purge()

    # clear error handling
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(CLEAR["MissingPermissions"])

def setup(bot):
    bot.add_cog(MessageCommands(bot))
