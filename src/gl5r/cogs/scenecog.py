#pre-doc: command group governing scene interactions; seat of the Scene Management service.
from discord.app_commands import command
from discord.ext.commands import GroupCog

class SceneCog(GroupCog,
              group_name='s',
              group_description='Scene Command Group',
              ):
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SceneCog, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        super(SceneCog, self).__init__()

    #to-do commands
        # key feature commands like skill and initiative controls belong to this cog.