from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

class DBManager(AsyncIOMotorClient):
    
    def __new__(cls, uri):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DBManager, cls).__new__(cls)
        return cls.instance
    
    def __init__(self, uri):
        super(DBManager, self).__init__()
        self.uri        = uri
        self.ServerApi  = ServerApi("1")

    # note: basic server connection confirmed--proper query structure needs building
    async def ping_server(self):
        try:
            self.admin.command('ping')
            print('ping operation successful')
        except Exception as e:
            print(e)
