from discord.ext.commands import bot
from config.global_settings import GlobalSettings
from config.intents import get_intents

def main():
    
    my_settings = GlobalSettings()

    gl5r = bot.Bot(
        command_prefix = '/',
        intents = get_intents(),
        )
    
    token = my_settings.get('bot_token')
    gl5r.run(token)

if __name__=='__main__':
    main()