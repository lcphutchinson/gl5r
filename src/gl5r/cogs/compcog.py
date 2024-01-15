#pre-doc: command group governing lookup calls
from discord.app_commands import command
from discord.ext.commands import GroupCog

class CompCog(GroupCog,
              group_name='l',
              group_description='Lookup Command Group',
              ):
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CompCog, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        super(CompCog, self).__init__()

    #to-do commands
        # these will follow the organization of compendium collections
        # in the database. Rules blurbs, Schools, Techniques, Items, etc
        # assessment of the necessity of multiple commands is still underway 