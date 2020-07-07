import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("날누르고 메시지 #할말")
    await client.change_presence(status=discord.Status.online, activity=game)
      

@client.event
async def on_message(message):
    if message.content.startswith("#"):
        msg = message.content[1:]
        await client .get_channel(int(730010475831623682)).send(msg)








client.run("BOT_TOKEN")
