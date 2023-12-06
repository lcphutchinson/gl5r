# pre-doc: prototype cog for general play commands. Eventually, commands without
# special context or privilege requirements will launch out of this cog.
from discord.ext import commands

class PlayCog(commands.Cog):

    def __init__(self, bot : commands.bot.Bot):
        self.bot = bot

    def __new__(cls, bot):
        if not hasattr(cls, 'instance'):
            cls.instance = super(PlayCog, cls).__new__(cls, bot)
        return cls.instance
    
    @commands.command
    async def hello(self, ctx):
        """Says Hello"""
        ctx.send("Hello!")

    async def register(self):
        self.bot.add_cog(self, self.bot)
    