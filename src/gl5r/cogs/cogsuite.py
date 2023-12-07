# pre-doc: provide logic here for initializing and registering each cog, so that
# GameLieutenant only needs one call to handle all its cog registration
from discord.ext.commands.bot import Bot
from gl5r.cogs.testcog import PlayCog

class Cogsuite():

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Cogsuite, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        pass
        # cogs can be created here as members of a list.
        # note: test adding registration to cog constructor