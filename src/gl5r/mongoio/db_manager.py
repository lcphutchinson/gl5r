from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

class DBManager(AsyncIOMotorClient):
    
    def __new__(cls, uri):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DBManager, cls).__new__(cls)
        return cls.instance
    
    def __init__(self, uri):
        super(DBManager, self).__init__()
        self.db = self.get_database('gl5r')
        self.ServerApi  = ServerApi("1")
        self.uri        = uri
        self.user_cache = dict()       
 
    # note: basic server connection confirmed--proper query structure needs building
    async def ping_server(self):
        try:
            self.admin.command('ping')
            print('ping operation successful')
        except Exception as e:
            print(e)

    async def get_user(self, user : str):
        if user in self.user_cache:
            return self.user_cache[user]
        else:
            pass # fetch the user data from the database
        # note: if the data isn't found, this is a new user. Run an insert to register.
        # self.user_cache[user] = doc that was fetched from the db.