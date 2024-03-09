# pre-doc: prefabricated base documents for shared ui prompts

def get(prompt: str):
    match(prompt):
        case 'sheet': 
            return {
                'message_title':'Character not found: Did you mean?',
                'options_dict': {},
                }
        case _:
            pass