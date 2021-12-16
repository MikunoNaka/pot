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

from cogs.mod_commands import ModCommands

# import ../phrases.py
try:
    from phrases import KICK_BAN
except ImportError:
    KICK_BAN = { 
        # error
        "MissingRequiredArgument": "Please specify a member for the action."
        , "MissingPermissions": "You don't have the permission to do so."
        , "MemberNotFound": "Member does not exist."
        , "CommandInvokeError": "Failed to kick user."
        , "unban_member_notfound": "Banned member {member} not found"

        # success
        , "member_kicked": "Member {member} has been kicked for reason \"{reason}\""
        , "member_banned": "Member {member} has been banned for reason \"{reason}\""
        , "member_unbanned": "User {member} has been unbanned."
    }

class ModCommandsErrHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # error handling for kick and ban
    @ModCommands.kick.error
    @ModCommands.ban.error
    async def kick_ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(KICK_BAN["MissingRequiredArgument"])

        if isinstance(error, commands.MissingPermissions):
            await ctx.send(KICK_BAN["MissingPermissions"])

        if isinstance(error, commands.MemberNotFound):
            await ctx.send(KICK_BAN["MemberNotFound"])

        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(KICK_BAN["CommandInvokeError"])

    # unban error handling
    @ModCommands.unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(KICK_BAN["MissingRequiredArgument"])

        if isinstance(error, commands.MissingPermissions):
            await ctx.send(KICK_BAN["MissingPermissions"])

def setup(bot):
    bot.add_cog(ModCommandsErrHandler(bot))
