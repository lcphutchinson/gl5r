# pre-doc: prototype cog for early development of user commands; will be left in
# for users to test resolver actions without a scene structure in place. 
from discord import Interaction
from discord.app_commands import command
from discord.ext.commands import GroupCog

class TestCog(GroupCog, 
              group_name='t', 
              group_description='Test Commands'
              ):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(TestCog, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        super(TestCog, self).__init__()

    @command(name='junk', description='a junk command for testing functionality')
    async def test(self, caller : Interaction):
        await caller.response.send_message("This was a test!", ephemeral=True)

    @command(name='roller', description='Manually call the dice roller')
    async def roll(self, caller : Interaction, rings : int, skills : int):   
        await caller.response.send_message("This command is under construction! try back later", ephemeral=True)
