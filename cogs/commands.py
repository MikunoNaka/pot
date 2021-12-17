# Pot - Discord bot which is pog. Pot.
# Version - 0.1
# Licensed under the MIT license - https://opensource.org/licenses/MIT
#
# Copyright (c) 2021 Vidhu Kant Sharma

import traceback
import discord
from discord.ext import commands

# to import from parent directory
import sys
sys.path.append('..')

# import ../phrases.py
try:
    from phrases import PING_MESSAGE
except ImportError:
    PING_MESSAGE = "pong"

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # handle all command exceptions
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('I do not know that command?!')
        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(PING_MESSAGE)

    @commands.command()
    async def ctx(self, ctx):
        await ctx.send(ctx.__dict__)
        print(ctx.__dict__)

def setup(bot):
    bot.add_cog(Commands(bot))
