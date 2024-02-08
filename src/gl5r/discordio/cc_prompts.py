from discord import SelectOption
from discord.interactions import Interaction
from discord.ui import Select, View

class SheetSelect(Select):
    def __init__(self):
        these_options=[
            SelectOption(
                label='Core Rulebook Sheet',
                default=True,
            ),
            SelectOption(
                label='Path of Waves Sheet',
            ),
        ]
        super(SheetSelect, self).__init__(
            max_values=1,
            min_values=1,
            options=these_options,
        )

    async def callback(self, caller : Interaction):
        pass # working on this logic

class SelectorView(View):
    def __init__(self, selector_type):
        super(SelectorView, self).__init__()
        self.add_item(selector_type())
