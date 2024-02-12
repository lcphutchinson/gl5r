# pre-doc: handle pre-launch configurations that require modification of the Bot object here,
# as well as operations like cog registration that are best handled asyncronously.
from discord.ext.commands.bot import Bot
from resources.intents import get_intents

class GLBot(Bot):

    def __new__(cls, token: str):
        if not hasattr(cls, 'instance'):
            cls.instance = super(GLBot, cls).__new__(cls)
        return cls.instance
    
    def __init__(self, token: str):
        super(GLBot, self).__init__(
            command_prefix='/',
            intents=get_intents(),
            )
        self.token = token
    
    # note: use on_ready only in development--final product should use a sync command
    async def on_ready(self):
        print('successfully logged in')
        await self.tree.sync()

    def launch(self):
        self.run(self.token)