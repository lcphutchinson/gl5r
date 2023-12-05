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

