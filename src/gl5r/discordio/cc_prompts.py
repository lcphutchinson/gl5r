from discord import SelectOption
from discord.interactions import Interaction
from discord.ui import Select, View

class QZero(Select):
    def __init__(self):
        q_zero_options = [
            SelectOption(label='Core Rulebook Sheet'),
            SelectOption(label='Path of Waves Sheet'),
        ]
        super(QZero, self).__init__(
            max_values=1,
            min_values=1,
            options=q_zero_options,
            placeholder='Select a Sheet Format',
        )
    async def callback(self, caller : Interaction):
        assert self.view is not None
        view : QPromptBuilder = self.view
        view.stop()

class QPromptBuilder(View):
    def __init__(self, q_type):
        super(QPromptBuilder, self).__init__()
        self.selector = q_type()
        self.add_item(self.selector)