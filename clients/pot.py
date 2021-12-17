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
    from phrases import ON_READY_MESSAGE
except ImportError:
    ON_READY_MESSAGE = "Logged in as {client_username}"
try:
    from phrases import BOT_STATUS
except ImportError:
    BOT_STATUS = "Yo doods I am Pot"

# this is a bot. and it's pog. POT
class Pot(commands.Bot):
    async def on_ready(self):
        print(ON_READY_MESSAGE.format(client_username=self.user.name))
        await self.client.change_presence(status=discord.Status.online, activity=discord.Game(BOT_STATUS))
