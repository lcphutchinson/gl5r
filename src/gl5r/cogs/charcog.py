# pre-doc: command group governing the user character list; seat of the Character Data Management service.
from discord.app_commands import command, describe, rename
from discord.ext.commands import GroupCog
from discord.interactions import Interaction
from mongoio.db_manager import DBManager
import discordio.cc_prompts as cc

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
    async def new_character(self, caller : Interaction, label : str):
        prompt = cc.QPromptBuilder(cc.QZero)
        await caller.response.send_message('Character Creation', view=prompt, ephemeral=True)
        await prompt.wait()
        print('operation successful')
        print(str(prompt.selector.values[0]))

    # slash command frame for easy copypastability 
    # @command(name='', description='')
    # @describe() 
    # @rename()
    async def nextcommand(source : Interaction):
        pass   
    
