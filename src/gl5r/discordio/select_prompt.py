from discord import SelectOption
from discord.interactions import Interaction
from discord.ui import Select, View

DEFAULT_TIMEOUT: float = 10.0

class SimpleSelect(Select):
    def __init__(self, **kwargs):
        super(SimpleSelect, self).__init__(**kwargs)

    async def callback(self, call: Interaction):    
        view: SelectorView = self.view
        view.reply = call
        view.stop()

class SelectorView(View):
    def __init__(self, selector_params: dict, **kwargs):
        super(SelectorView, self).__init__(**kwargs)
        self.reply: Interaction = None
        self.selector: Select = self.build_selector(selector_params)
        self.add_item(self.selector)
        self.timeout = DEFAULT_TIMEOUT

    def build_selector(self, params: dict):
        options_data: dict = params.pop('options_dict')
        options: dict = self.build_options(options_data)
        params.update(options)
        return SimpleSelect(**params)

    def build_options(self, options_data: dict):
        options: list[SelectOption] = []
        for [label, descriptor] in options_data.items():
            option = SelectOption(label=label, description=descriptor)
            options.append(option)
        return {'options':options}

async def launch_select_prompt(call: Interaction, prompt_params: dict):
    await call.response.defer(ephemeral=True, thinking=True)
    message: str = prompt_params.pop('message_title')
    prompt = SelectorView(selector_params=prompt_params)
    response = await call.followup.send(content=message, view=prompt, wait=True)
    timeout: bool = await prompt.wait()
    await response.delete()
    if not timeout: return prompt
    else: return

        
