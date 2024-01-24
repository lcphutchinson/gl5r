# pre-doc: command group governing the user character list; seat of the Character Data Management service.
from discord.app_commands import command
from discord.ext.commands import GroupCog

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

    #to-do commands:
        # character list commands (new, list, select, retire, etc) but also commands for spending
        # experience points and other character resources to update the sheet, go here.

    
    