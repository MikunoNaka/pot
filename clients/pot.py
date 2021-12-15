from discord.ext import commands

# this is a bot. and it's pog. POT
class Pot(commands.Bot):
    async def on_ready(self):
        print("Logged in as", self.user.name, "(id=" + str(self.user.id) + ")")
