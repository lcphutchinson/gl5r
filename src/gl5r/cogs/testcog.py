# pre-doc: prototype cog for non-slash user test commands: decontextualized
# skill checks, manual rolls, and anything outside of normal command parameters. 
from discord.ext.commands import GroupCog
from discord import app_commands
from discord import Interaction

class TestCog(GroupCog, 
              group_name='t', 
              group_description='Test Commands'):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(TestCog, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        super(TestCog, self).__init__()

    # note: this format can't be used for ui-supported slash commands.
    @app_commands.command(name='truetest', description='a junk command for testing functionality')
    async def test(self, int : Interaction):
        await int.response.send_message("This was a test!")

    