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
    from phrases import KICK_BAN, INVALID_USERNAME_MESSAGE
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

    INVALID_USERNAME_MESSAGE = "Invalid user. correct format is USER#1234"

class ModCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # kicking a member
    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(KICK_BAN["member_kicked"].format(member=member, reason=reason))

    # banning a member
    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(KICK_BAN["member_banned"].format(member=member, reason=reason))

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

    # unbanning a member
    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await(ctx.guild.bans())

        try:
            member_name, member_discriminator = member.split("#")
        except ValueError:
            await ctx.send(INVALID_USERNAME_MESSAGE)
            return

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(KICK_BAN["member_unbanned"].format(member=user.mention))
                return
        # if member not in ban_entry
        await ctx.send(KICK_BAN["unban_member_notfound"].format(member=member))

    # unban error handling
    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(KICK_BAN["MissingRequiredArgument"])

        if isinstance(error, commands.MissingPermissions):
            await ctx.send(KICK_BAN["MissingPermissions"])

def setup(bot):
    bot.add_cog(ModCommands(bot))
