from discord import Intents

def get_intents():
    
    my_intents = Intents.default()
    my_intents.auto_moderation                  = False
    my_intents.auto_moderation_configuration    = False
    my_intents.auto_moderation_execution        = False
    my_intents.bans                             = False
    my_intents.dm_messages                      = False
    my_intents.dm_reactions                     = False
    my_intents.dm_typing                        = False
    my_intents.emojis                           = False
    my_intents.emojis_and_stickers              = False
    my_intents.guild_messages                   = False
    my_intents.guild_reactions                  = False
    my_intents.guild_scheduled_events           = False
    my_intents.guild_typing                     = False
    my_intents.guilds                           = False
    my_intents.integrations                     = False
    my_intents.invites                          = False
    my_intents.members                          = False     # Privileged Intent
    my_intents.message_content                  = True      # Privileged Intent
    my_intents.messages                         = False
    my_intents.moderation                       = False
    my_intents.presences                        = False     # Privileged Intent
    my_intents.reactions                        = False
    my_intents.typing                           = False
    my_intents.voice_states                     = False
    my_intents.webhooks                         = False

    return my_intents