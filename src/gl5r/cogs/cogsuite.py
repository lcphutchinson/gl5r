# pre-doc: provide logic here for initializing and registering each cog, so that
# GameLieutenant only needs one call to handle all its cog registration
from discord.ext.commands.bot import Bot
from .charcog import CharCog
from .testcog import TestCog

class Cogsuite():

    def __new__(cls, bot: Bot):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Cogsuite, cls).__new__(cls)
        return cls.instance
    
    def __init__(self, bot: Bot):
        self.bot = bot
        self.suite = [
            CharCog(),
            TestCog(),
        ]
        # cogs can be created here as members of a list.
        # note: test adding registration to cog constructor

    async def register_all(self):
        for cog in self.suite:
            await self.bot.add_cog(cog)
