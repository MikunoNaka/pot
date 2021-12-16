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
    from phrases import KICK_BAN
except ImportError:
    KICK_BAN = {
        "MissingRequiredArgument": "Please specify a member for the action."
        , "MissingPermissions": "You don't have the permission to do so."
        , "MemberNotFound": "Member does not exist."
        , "CommandInvokeError": "Failed to kick user."
    }


class ModCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # kicking a member
    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)

    # banning a member
    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)

    # error handling for kick and ban
    @kick.error
    @ban.error
    async def kick_ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(KICK_BAN["MissingRequiredArgument"])

        if isinstance(error, commands.MissingPermissions):
            await ctx.send(KICK_BAN["MissingPermissions"])

        if isinstance(error, commands.MemberNotFound):
            await ctx.send(KICK_BAN["MemberNotFound"])

        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(KICK_BAN["CommandInvokeError"])

def setup(bot):
    bot.add_cog(ModCommands(bot))
