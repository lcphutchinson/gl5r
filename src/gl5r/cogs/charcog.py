# pre-doc: command group governing user-character registration an the user character list.
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
        # sheet // fetch a record of the active character
        # list // list characters
        # select // choose a new active character
        # new // launch character creator
        # retire // relinquish ownership of a character
        # adopt // initiate adoption process for an unclaimed character

        # note: consider difflib for producing close matches where character name inputs are used

    