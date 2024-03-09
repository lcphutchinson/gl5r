from .cc_record import CCQueryRecord
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

class DBManager(AsyncIOMotorClient):
    def __new__(cls, uri: str=None):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DBManager, cls).__new__(cls)
            cls.instance.is_configured = False
        return cls.instance

    def __init__(self, uri: str=None):
        if self.is_configured: return
        super(DBManager, self).__init__(uri)
        self.ServerApi  = ServerApi('1')
        self.is_configured = True

    async def get_cc_query(self, user: int, label: str=None):
        collection = self.db.get_collection('cc_data')
        query: dict = {'author': user, 'cc_complete': False}
        results = {}
        try:
            async for doc in collection.find(query):
                results += doc
        except Exception as e:
            print(repr(e))
        finally:
            if not results: return None
            cc_record = CCQueryRecord(results)
            print(repr(results)) # test
            



        