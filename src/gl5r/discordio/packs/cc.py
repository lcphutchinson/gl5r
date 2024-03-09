# pre-doc: pre-fabricated base arguments for select_prompt to generate
# character creation prompts. In GL, these will be pulled from the system db

def get(q: int):
    match q:
        case 0:
            return {
                'message_title': 'Create a New Character',
                'options_dict': {
                    'Core Rulebook Sheet': None, 
                    'Path of Waves Sheet': None,
                },
                'placeholder': 'Select a Sheet Format',
        }
        case _:
            pass