# pre-doc: provide logic here for initializing and registering each cog, so that
# GameLieutenant only needs one call to handle all its cog registration
from discord.ext.commands.bot import Bot
from .cc_cog import CCCog

class Cogsuite():

    def __new__(cls, bot: Bot):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Cogsuite, cls).__new__(cls)
            cls.is_configured = False
        return cls.instance
    
    def __init__(self, bot: Bot):
        if self.is_configured: return
        self.bot = bot
        self.suite = [
            CCCog(),
        ]
        self.is_configured = True
        # cogs can be created here as members of a list.
        # note: test adding registration to cog constructor

    async def register_all(self):
        for cog in self.suite:
            await self.bot.add_cog(cog)
