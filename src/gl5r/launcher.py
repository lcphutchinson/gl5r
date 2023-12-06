# pre-doc: configure and verify proper function of system components from this script, then launch the bot.
from config.global_settings import GlobalSettings
from game_lieutenant import GameLieutenant

def main():
    
    my_settings = GlobalSettings()
    this_bot = GameLieutenant()

    token = my_settings.get('bot_token')
    this_bot.run(token)

if __name__=='__main__':
    main()