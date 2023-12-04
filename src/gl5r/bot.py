from config.intents import get_intents
import config.global_settings as config
import discord as dpy

def main():
    client = dpy.Client(intents=get_intents())
    my_settings = config.GlobalSettings()

    @client.event
    async def on_ready():
        return
    
    @client.event
    async def on_message(message):
        pass
    #    await route(message)
        

    token = my_settings.get("bot_token")
    client.run(token)

if __name__=="__main__":
    main()