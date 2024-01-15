# pre-doc: handle pre-launch configurations that require modification of the Bot object here,
# as well as operations like cog registration that are best handled asyncronously.
from discord.ext.commands.bot import Bot
from resources.intents import get_intents

from discord.app_commands import CommandTree #testing

class GLBot(Bot):

    def __new__(cls, token):
        if not hasattr(cls, 'instance'):
            cls.instance = super(GLBot, cls).__new__(cls)
        return cls.instance
    
    def __init__(self, token):
        super(GLBot, self).__init__(
            command_prefix= '/',
            intents= get_intents()
            )
        self.token = token
    
    # note: remove this if no more useful functionality comes along for on_ready
    async def on_ready(self):
        print('successfully logged in')
        await self.tree.sync()              # use sync() in on_ready only during early dev

    def launch(self):
        self.run(self.token)