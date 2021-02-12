import discord
import os
import asyncio
from keep_alive import keep_alive

class MyClient(discord.Client):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.roles = {
      'initiant': 809568040902852639
    }

  async def on_ready(self):
    print('------')
    print('Logged in as {0}'.format(self.user.name))
    print(self.user.id)
    print('------')

  async def on_member_join(self, member):
    guild = member.guild

    if guild is None:
      # Check if we're still in the guild and it's cached.
      return
    
    role = guild.get_role(self.roles['initiant'])
    if role is None:
      # Make sure the role still exists and is valid.
      return
    
    try:
      # Finally add the role
      await member.add_roles(role)
    except discord.HTTPException:
      pass

    if guild.system_channel is not None:
      await asyncio.sleep(5)

      to_send = 'Blub, blub... Blub! Blubba bloop. Blub.\n > **Translation**\n > Foul greetings to you, oh {0.mention}, oh witless charlatan... You who have been generously granted the distinguished opportunity to serve _{1.name}_, be a good underling and wait silently here. The master\'s warden is arranging for your new home and desigation as we speak.'.format(member, guild)
      
      await guild.system_channel.send(to_send)
  
  async def on_group_join(channel, user):
    print(channel, user)

intents = discord.Intents.default()
intents.members = True
client = MyClient(intents=intents)

keep_alive()
client.run(os.getenv('TOKEN'))
