# you can ignore most of these comments nick helped make it less braindead
# but im keeping them because I like reading my tired comments

# I should pep8 this but its too far gone 
# thank god most of you don't understand this, this entire code is pretty braindead but 
# it works sooooo....
import os
import logging

import aiohttp
from discord.ext import commands

from webserver import keep_alive


logging.basicConfig(level=logging.INFO)


class TreePaunchBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='~')
        self.owner_ids = [680835476034551925, 258013196592349184]
        self.session = aiohttp.ClientSession()
        self.load_extension('streamobserver')
        print("TreePaunchBot started")

    async def on_command_error(self, ctx, error):
        print(error)
        return True

keep_alive()
TOKEN = os.environ.get("DISCORD_TOKEN")
TreePaunchBot().run(TOKEN)
