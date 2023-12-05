from dotenv import load_dotenv
from os import environ as env

class GlobalSettings:
    settings_dict = None

    def __init__(self):
        load_dotenv()
        self.settings_dict = {
            'bot_token': env.get('bot_token'),
            'mongo_uri': env.get('mongo_uri')
        }

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(GlobalSettings, cls).__new__(cls)
        return cls.instance
    
    def get(self, key : str):
        return self.settings_dict[key]
    