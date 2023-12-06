# pre-doc: handle pre-launch configurations that require modification of the Bot object here,
# as well as operations like cog registration that are best handled asyncronously.
from discord.ext.commands.bot import Bot
from config.intents import get_intents

class GameLieutenant(Bot):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(GameLieutenant, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        super(GameLieutenant, self).__init__(
            command_prefix= '/',
            intents= get_intents()
            )
    
    async def on_ready(self):
        print('successfully logged in')

