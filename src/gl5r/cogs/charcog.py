# pre-doc: command group governing the user character list; seat of the Character Data Management service.
from discord.app_commands import command, describe, rename
from discord.ext.commands import GroupCog
from discord.interactions import Interaction
from discordio.cc_prompts import QView
from mongoio.db_manager import DBManager

class CharCog (GroupCog, 
               group_name='c',
               group_description='Character List Command Group'
               ):
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CharCog, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        super(CharCog, self).__init__()
        self.db_link = DBManager(uri=None) # DBManager will already have a uri

    #to-do commands:
        # character list commands (new, list, select, retire, etc) but also commands for spending
        # experience points and other character resources to update the sheet, go here.

    @command(name='create', description='create a new, empty character sheet')
    @describe(label='a temporary label for this sheet') 
    async def new_character(self, call : Interaction, label : str):
        await call.response.defer(ephemeral=True, thinking=True)
        prompt = QView({'Question':0})
        response = await call.followup.send(f'New Character: "%s"' %label, view=prompt, wait=True)
        timeout : bool = await prompt.wait()
        await response.delete()
        if not timeout:
            call: Interaction = prompt.reply
            await call.response.defer(ephemeral=True, thinking=True)
            q_data: dict = {
                'author': str(call.user.id),
                'label' : label,
                'type'  : prompt.selector.values[0]
            }
            # some_db_command = some'build_a_db_command'function(q_data)
            # results = await self.db_link.do_some_command(some_db_command)
            # await call.followup.send(success_or_failure_msg)
            print(q_data) #test
            await call.followup.send('Next steps under construction :thumbsup:')

    # slash command frame for easy copypastability 
    # @command(name='', description='')
    # @describe() 
    # @rename()
    async def nextcommand(call : Interaction):
        pass   
    
