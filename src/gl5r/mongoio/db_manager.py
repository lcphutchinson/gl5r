from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

class DBManager(AsyncIOMotorClient):
    
    def __new__(cls, uri: str):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DBManager, cls).__new__(cls)
        return cls.instance
    
    def __init__(self, uri: str):
        super(DBManager, self).__init__(uri)
        self.ServerApi  = ServerApi('1')   

    # note: deprecated example method
    async def get_user(self, user : str):
        if user in self.user_cache:
            return self.user_cache[user]
        user_id = { '_id': user }
        try:
            user_doc = await self.db.users.find_one(user_id)
            if user_doc:
                return user_doc
            
            await self.db.users.insert_one(user_id)
            self.user_cache[user] = user_id                 # remember to limit cache growth
            return user_id
        
        except Exception as e:
            pass # logic for timeouts goes here
        
    