from Token import Token as Tk
import interactions 
import time
import discord
import Embeds
import datetime
import random

class Main_Client():
    def __init__(self):
        self.Client = interactions.Client(Tk)
    def Start(self):
        self.Client.start()
    pass

Interaction_Client = Main_Client()

@Interaction_Client.Client.event()
async def on_ready():
    print(f"Bot Is Online At {datetime.datetime.now()}")

@Interaction_Client.Client.command(description='Delete Recent Messages')
@interactions.option(description='Enter A Integer (Max:10)')
async def clear(ctx:interactions.CommandContext,amount:int):
    match amount:
        case 0:
            await ctx.send(embeds=Embeds.clear_embed_error)
            time.sleep(60)
            await ctx.channel.purge(1)
    pass
    if amount > 0 and amount <= 10:
        await ctx.channel.purge(amount)
        await ctx.send(embeds=Embeds.clear_embed)
        time.sleep(60)
        await ctx.channel.purge(1)

@Interaction_Client.Client.command(description='Preview Your Own Avatar')
async def avatar(ctx,member:discord.Member=None):
    member = ctx.author if not member else member
    avatar_embed = interactions.Embed(
        title='📷 Avatar',
        description=None,
        color=0x00FF00)
    avatar_embed.add_field(
        name='Avatar Slash Command:',
        value='```yaml\nHere You Go !\n```'
    )
    avatar_embed.set_image(member.avatar_url)
    await ctx.send(embeds=avatar_embed)

@Interaction_Client.Client.command(description='8Ball !')
@interactions.option(description='Ask Any Question Or Anything !')
async def sikrox(ctx:interactions.CommandContext,question:str):
    Possibilities_Number = random.randint(0 , 100)
    await ctx.send(f'```yaml\nQuestion : {question}\nPossibility : {Possibilities_Number}%\n```')

Interaction_Client.Start()