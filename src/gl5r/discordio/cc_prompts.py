# pre-doc: discord's ui views and view components for the 'Game of Twenty Questions'
# are constructed and delivered from this module. If possible, include long-form 
# description prompts alongside selector prompts
from discord import SelectOption
from discord.interactions import Interaction
from discord.ui import Modal, Select, View

class FollowupModal(Modal):
    pass

class TwentyQuestionsSelector(Select):
    def __init__(self, followup: FollowupModal=None, **kwargs):
        super(TwentyQuestionsSelector, self).__init__(**kwargs)
        self.followup = followup
    async def callback(self, call: Interaction):
        if self.followup:
            pass # wip
        else:
            view : QView = self.view
            view.reply = call
            view.stop()

class QView(View): # q : int will be replaced with a dict later, for questions with conditional selectors
    def __init__(self, q: dict, **kwargs):
        super(QView, self).__init__(**kwargs)
        self.reply: Interaction = None
        self.selector = self.get_selector(q)
        self.add_item(self.selector)

    def get_selector(self, params: dict):
        q: int = params.pop('Question')
        match q:
            case 0:
                params = { 
                    'options': [
                    SelectOption(label='Core Rulebook Sheet'),
                    SelectOption(label='Path of Waves Sheet'),
                    ],
                    'placeholder': 'Select a Sheet Format',
                    }
            
            case _:
                pass
        return TwentyQuestionsSelector(**params)
    
                