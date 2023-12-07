# pre-doc: prototype cog for general play commands. Eventually, commands without
# special context or privilege requirements will launch out of this cog.
from discord.ext import commands

class TestCog(commands.Cog):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(TestCog, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        super(TestCog, self).__init__()

    @commands.command()
    async def test(self, ctx):
        print("event fired!")
        await ctx.send("This was a test!")

    