# pre-doc: command group governing character creation functions
from discord.app_commands import command, describe, rename
from discord.ext.commands import GroupCog
from discord.interactions import Interaction
from discordio.select_prompt import SelectorView
from mongoio.cc_record import CCQueryRecord, CCRecord
from mongoio.db_manager import DBManager
import discordio.packs as packs

class CCCog (GroupCog, 
               group_name='cc',
               group_description='Character Creation Command Group'
               ):
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CCCog, cls).__new__(cls)
            cls.is_configured = False
        return cls.instance
    
    def __init__(self):
        if self.is_configured: return
        super(CCCog, self).__init__()
        self.db_link = DBManager()
        self.is_configured = True

    # pre-doc: central commmand for read, write, and update functions in the CC context
    @command(name='answer', description='answer a character creation question')
    @describe(sheet_label='the character to work on', question='the question to jump to (optional)') 
    @rename(sheet_label='for')
    async def pull_question(self, call: Interaction, sheet_label: str, question: int=None):
        await call.response.defer(ephemeral=True, thinking=True)
        caller: str = str(call.user.id) # str for ease of storage
        cc_query: CCQueryRecord = await self.db_link.get_cc_query(caller)
        if not cc_query:
            # Case issue imminent: Null cc_query can mean no items found OR query failed--fix.
            return
        cc_data: CCRecord = cc_query.reduce_to(sheet_label)
        if not cc_data:
            # Case: User mispelled their sheet label
            # consider a request_clarity() function to pull this block out
            clarity_pack = packs.clarity.get('sheet')
            for key in cc_query.records:
                clarity_pack['options_dict'].update({key:None})
            clarify_prompt: SelectorView = self.launch_cc_prompt(call, clarity_pack)
            if clarify_prompt:
                sheet_label = clarify_prompt.selector.values[0]
                cc_data = cc_query.reduce_to(sheet_label)
                call = clarify_prompt.reply
            else: return 
        # next steps: build insertion fields into CCRecord to support an
        # update() method that commits changes back to the db.
        call.followup.send('Next steps under construction :thumbsup:')


    @command(name='create', description='create a new, empty character sheet')
    @describe(label='a temporary label for this sheet') 
    async def new_character(self, call: Interaction, label: str):
        return self.pull_question(call, label, 0)

    # slash command frame for easy copypastability 
    # @command(name='', description='')
    # @describe() 
    # @rename()
    async def nextcommand(self, call : Interaction):
        pass   
    
