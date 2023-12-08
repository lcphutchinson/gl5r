# pre-doc: configure and verify proper function of system components from this script, then launch the bot.
import asyncio
from config.global_settings import GlobalSettings
from mongoio.db_manager import DBManager
from cogs.cogsuite import Cogsuite 
from gl_bot import GLBot

def main():
    
    my_settings = GlobalSettings()
    my_token    = my_settings.get('bot_token')
    my_uri      = my_settings.get('mongo_uri')
    
    this_db     = DBManager(my_uri)
    this_bot    = GLBot(my_token)
    
    my_cogs     = Cogsuite(this_bot)
    asyncio.run(my_cogs.register_all())

    this_bot.launch()

if __name__=='__main__':
    main()