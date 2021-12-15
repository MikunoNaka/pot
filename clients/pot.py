# Pot - Discord bot which is pog. Pot.
# Version - 0.1
# Licensed under the MIT license - https://opensource.org/licenses/MIT
#
# Copyright (c) 2021 Vidhu Kant Sharma

from discord.ext import commands

# this is a bot. and it's pog. POT
class Pot(commands.Bot):
    async def on_ready(self):
        print("Logged in as", self.user.name, "(id=" + str(self.user.id) + ")")
