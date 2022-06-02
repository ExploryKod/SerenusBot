from bot_serenus_V2 import Root
import discord
client = discord.Client()
import re

class Bot(discord.Client):
    
    @client.event
    async def on_ready():
        print("le bot est connecté.")

    @client.event
    async def on_member_join(member):
        general_channel: discord.TextChannel = client.get_channel(978578279374147614)
        await general_channel.send(content=f"Bienvenue sur le serveur {member.display_name} !")

    @client.event
    async def on_message(message):
        message.content = message.content.lower()

        if message.author == client.user:
            return

        Help_channel = client.get_channel(978578279374147614)

        if message.channel == Help_channel and message.content.startswith('$help'):
            await Help_channel.send(Root.user_response())

        if message.content == "del":
            await message.channel.purge(limit=3)
        
        
        # check call for !serenus command
        args = message.content.split()

        if args[0] == '!!serenus':
            # 2 scenarios :
            # - 1 more argument and argument == help
            # - x more arguments of type user id
            if len(args) == 2 and args[1] == 'help':
                await message.channel.send('Quels sont vos besoins')
                await message.channel.send('Dites nous comment nous pouvons vous aider \n`!Serenus Trouver le sommeil`\n`!Serenus Equilibre émotionnelle`\n`!Serenus Faire face à la dépression`\n`!Serenus Briser la solitude`')
            elif len(args) >= 2:
                # check if all arguments are valid member tags
                valid_member_tags = True
                for arg in args[1:]:
                    try:
                        member_id = re.search('<@!(.+?)>', arg).group(1)
                    except:
                        valid_member_tags = False
                        break

                if not valid_member_tags:
                    await message.channel.send('<@!{0}> all arguments must be valid user tags, for help please use `!serenus help`'.format(message.author.id))
                    return

                # if all is ok, send them a serenus, cheers !
                for member_tag in args[1:]:
                    await message.channel.send('{0}, here is a serenus for you ! :hot_serenus:'.format(member_tag))
            else:
                # with no argument send a notification to author
                await message.channel.send('<@!{0}> not enough arguments, for help please use `!!serenus help`'.format(message.author.id))

        #await client.process_commands(message)

client.run("OTc4MjI4ODkwMDU1MDgyMDI1.Gsun_9.QjTiVsPsfGIfeWBd-yWB0pTKOkjgty4k_gcSiY")