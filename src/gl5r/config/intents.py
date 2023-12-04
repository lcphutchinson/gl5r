"""docstring"""

import discord as dpy

def get_intents():
    
    intents = dpy.Intents.default()
    intents.auto_moderation                 = False
    intents.auto_moderation_configuration   = False
    intents.auto_moderation_execution       = False
    intents.bans                            = False
    intents.dm_messages                     = False
    intents.dm_reactions                    = False
    intents.dm_typing                       = False
    intents.emojis                          = False
    intents.emojis_and_stickers             = False
    intents.guild_messages                  = False
    intents.guild_reactions                 = False
    intents.guild_scheduled_events          = False
    intents.guild_typing                    = False
    intents.guilds                          = False
    intents.integrations                    = False
    intents.invites                         = False
    intents.members                         = False     # Privileged Intent
    intents.message_content                 = True      # Privileged Intent
    intents.messages                        = False
    intents.moderation                      = False
    intents.presences                       = False     # Privileged Intent
    intents.reactions                       = False
    intents.typing                          = False
    intents.value                           = False
    intents.voice_states                    = False
    intents.webhooks                        = False

    return intents