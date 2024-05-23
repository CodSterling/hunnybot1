import discord
from discord.ext import commands
import random
import asyncio
import json
from discord import colour

# Configure intents before creating bot instance
intents = discord.Intents.default()
intents.members = True
intents.reactions = True
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)


@bot.event
async def on_ready():
    print(f'Badass Bot is running!')

    channel = bot.get_channel(1205712688626409523)
    if channel:
        embed = discord.Embed(
            title="WELCOME TO THE\n"
                  "BUNNY KINGDOM ADVENTURE!\n\n"
                  "",
            description="*** use .hop to start***",
            color=discord.Color.purple()
        )
        embed.add_field(name=f'***BORKNY POEM***', value=f'***{script}***', inline=False)
        # Add fields to the embed
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/1205749795268861962/1235027565895352360/10.gif?ex=6632e08d&is=66318f0d&hm=e99c1bb336167b286e30d719afe52a21716ee8f83f383878f08466f5807a3e08&")
        await channel.send(embed=embed)
    else:
        print("Channel not found")


@bot.command(name="start")
async def start(ctx):
    channel = bot.get_channel(1205712688626409523)
    if channel:
        embed = discord.Embed(
            title="WELCOME TO THE\n"
                  "BUNNY KINGDOM ADVENTURE!!\n\n"
                  "",
            description="*** use .hop to start***",
            color=discord.Color.purple()
        )
        embed.add_field(name=f'***BORKNY POEM***', value=f'***{script}***', inline=False)
        # Add fields to the embed
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/1205749795268861962/1235027565895352360/10.gif?ex=6632e08d&is=66318f0d&hm=e99c1bb336167b286e30d719afe52a21716ee8f83f383878f08466f5807a3e08&")
        await channel.send(embed=embed)
    else:
        print("Channel not found")


def load_token():
    with open('token2.json', 'r') as f:
        config = json.load(f)
        return config['token']


@bot.listen()
async def on_message(message):
    if message.author == bot.user:
        pass
    # Define the word-to-emoji mapping
    word_emoji_map = {
        'hunnys': '❤️',  # Heart emoji
        'dream': '☁️',
        'hypno': ' 🍥 ',  # Cloud emoji
        'morning': '☀️',  # Sun emoji
        'hello': '👋'
    }

    # Check each word in the message
    for word, emoji in word_emoji_map.items():
        if word in message.content.lower():  # Case-insensitive check
            await message.add_reaction(emoji)


script = "⋋⁠✿⁠ ⁠⁰⁠ ⁠o⁠ ⁠⁰⁠ ⁠✿⁠⋌(⁠ʘ⁠ᗩ⁠ʘ⁠’⁠)✧⁠\⁠(⁠>⁠o⁠<⁠)⁠ﾉ⁠✧\nლ⁠(⁠^⁠o⁠^⁠ლ⁠)ヽ⁠༼⁠⁰⁠o⁠⁰⁠；⁠༽⁠ノლ⁠(⁠^⁠o⁠^⁠ლ⁠)(⁠´⁠⊙⁠ω⁠\n⊙⁠`⁠)⁠！⊙⁠.⁠☉(ﾟ⁠οﾟ⁠人⁠)⁠)(⁠´⁠(⁠ｪ⁠)⁠｀⁠）ʕ⁠·⁠ᴥ⁠·⁠ʔヾ⁠(⁠*⁠\n⁠Ｏ⁠’⁠*⁠)⁠/ᕙ⁠[⁠･⁠۝･⁠]⁠ᕗᕙ⁠(⁠ ͡⁠◉⁠ ͜⁠ ⁠ʖ⁠ ͡⁠◉⁠)⁠ᕗ"


@bot.command(name="hop")
async def hop(ctx):
    embed = discord.Embed(title="WELCOME! \n"
                                "You must help COD navigate the BUNNY KINGDOM!\n\n"
                                "Help Cod find his way to his HUNNY'S house!\n", color=0x800080)
    embed.add_field(name=f"Carmen Electron's address is not listed\n"
                         f"****Time to choose a direction!****\n"
                         f"***Use .left, .right, .up or .down to begin!***",
                    value="", inline=False)
    embed.add_field(name=f'***BORNKY POEM***', value=f'***{script}***', inline=False)
    embed.set_image(
        url="https://cdn.discordapp.com/attachments/1205749795268861962/1243003612557348864/749b1181-b6c0-4094-8c94-0224bd1e5b7d.jpeg?ex=664fe4d3&is=664e9353&hm=607533741e124485f26c28367e4adc9c3d860de13c56ec8196849d4c25580a63&")
    await ctx.send(embed=embed)

outcomes = ["pass", "blocked", "trapped", "door"]
images = [
    "https://cdn.discordapp.com/attachments/1205749795268861962/1243003351738613770/Hunny_8792.png?ex=664fe494&is=664e9314&hm=f9468e389ba0f21701f92d09ab4f07778bd8595ba58fb2a812a072f2cd5997cf&",
    "https://cdn.discordapp.com/attachments/1205749795268861962/1243003352250323004/Hunny_3679.png?ex=664fe495&is=664e9315&hm=aa6dae784d732bfed02075d2d1857e72b0ec4d25d4d223dd69aff7f592d8e570&",
    "https://cdn.discordapp.com/attachments/1205749795268861962/1243003352808427571/Hunny_3930.png?ex=664fe495&is=664e9315&hm=3ff8323604970fe4ad06f7df987668fa842bb773d185e38d26994045fa64a541&",
    "https://cdn.discordapp.com/attachments/1205749795268861962/1243004330693361786/Hunny_1057.png?ex=664fe57e&is=664e93fe&hm=3ce0a0dee81075554ff3f4a0c5e0936c99ba940c45e8c82ce6d5cc20e9f4afd8&"
]
names = ["Ava Serling", "Lila Davenport", "Maya Vance", "Zara Knight", "Tessa Blake"]
compliments = ["Your outfit is so on-trend!",
               "LOVE your hair!",
               "You make style look easy!",
               "LOVE your look so much!!"]


@bot.command(name="left")
async def left(ctx):
    print("Left command received")  # Debugging line
    outcome = random.choice(outcomes)

    # Create a base embed
    embed = discord.Embed(color=discord.Color.blue())

    if outcome == "pass":
        embed.title = "Outcome: Pass"
        embed.description = ("You pass through safely.\n\n"
                             "Please choose a new direction\n"
                             "use .left, .right, .up or .down")
        embed.colour = discord.Color.green()
    elif outcome == "blocked":
        embed.title = "Outcome: Blocked"
        embed.description = ("You are blocked by an obstacle.\n\n"
                             "Please choose a new direction\n"
                             "use .left, .right, .up or .down")
        embed.colour = discord.Color.red()
    elif outcome == "trapped":
        embed.title = "Outcome: Trapped"
        embed.description = ("You are trapped and can't move.\n"
                             "use .free to FREE YOURSELF!")
        embed.colour = discord.Color.orange()
    elif outcome == "door":
        embed.title = "Outcome: Door"
        embed.description = "Use .wakeup to help Cod wake up!"
        embed.colour = discord.Color.blue()
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/1205749795268861962/1243003351306866749/Screenshot_2023-11-01_085038.png?ex=664fe494&is=664e9314&hm=54c7a97972bbd4058c92f0339c57699cfdd185b767a3e2512c4fac8dcb7e4130&")
    # Add additional field and image
    hunny_name = random.choice(names)
    your_compliment = random.choice(compliments)
    embed.add_field(name=f'You run into a fashionable Hunny, {hunny_name}', value=f'She says, {your_compliment}', inline=False)
    img = random.choice(images)
    embed.set_image(url=img)

    await ctx.send(embed=embed)

@bot.command(name="right")
async def right(ctx):
    print("Left command received")  # Debugging line
    outcome = random.choice(outcomes)

    # Create a base embed
    embed = discord.Embed(color=discord.Color.blue())

    if outcome == "pass":
        embed.title = "Outcome: Pass"
        embed.description = ("You pass through safely.\n\n"
                             "Please choose a new direction\n"
                             "use .left, .right, .up or .down")
        embed.colour = discord.Color.green()
    elif outcome == "blocked":
        embed.title = "Outcome: Blocked"
        embed.description = ("You are blocked by an obstacle.\n\n"
                             "Please choose a new direction\n"
                             "use .left, .right, .up or .down")
        embed.colour = discord.Color.red()
    elif outcome == "trapped":
        embed.title = "Outcome: Trapped"
        embed.description = ("You are trapped and can't move.\n"
                             "use .free to FREE YOURSELF!")
        embed.colour = discord.Color.orange()
    elif outcome == "door":
        embed.title = "Outcome: Door"
        embed.description = "Use .wakeup to help Cod wake up!"
        embed.colour = discord.Color.blue()
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/1205749795268861962/1243003351306866749/Screenshot_2023-11-01_085038.png?ex=664fe494&is=664e9314&hm=54c7a97972bbd4058c92f0339c57699cfdd185b767a3e2512c4fac8dcb7e4130&")
    # Add additional field and image
    hunny_name = random.choice(names)
    your_compliment = random.choice(compliments)
    embed.add_field(name=f'You run into a fashionable Hunny, {hunny_name}', value=f'She says, {your_compliment}',
                    inline=False)
    img = random.choice(images)
    embed.set_image(url=img)

    await ctx.send(embed=embed)


@bot.command(name="up")
async def up(ctx):
    print("Left command received")  # Debugging line
    outcome = random.choice(outcomes)

    # Create a base embed
    embed = discord.Embed(color=discord.Color.blue())

    if outcome == "pass":
        embed.title = "Outcome: Pass"
        embed.description = ("You pass through safely.\n\n"
                             "Please choose a new direction\n"
                             "use .left, .right, .up or .down")
        embed.colour = discord.Color.green()
    elif outcome == "blocked":
        embed.title = "Outcome: Blocked"
        embed.description = ("You are blocked by an obstacle.\n\n"
                             "Please choose a new direction\n"
                             "use .left, .right, .up or .down")
        embed.colour = discord.Color.red()
    elif outcome == "trapped":
        embed.title = "Outcome: Trapped"
        embed.description = ("You are trapped and can't move.\n"
                             "use .free to FREE YOURSELF!")
        embed.colour = discord.Color.orange()
    elif outcome == "door":
        embed.title = "Outcome: Door"
        embed.description = "Use .wakeup to help Cod wake up!"
        embed.colour = discord.Color.blue()
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/1205749795268861962/1243003351306866749/Screenshot_2023-11-01_085038.png?ex=664fe494&is=664e9314&hm=54c7a97972bbd4058c92f0339c57699cfdd185b767a3e2512c4fac8dcb7e4130&")
    # Add additional field and image
    hunny_name = random.choice(names)
    your_compliment = random.choice(compliments)
    embed.add_field(name=f'You run into a fashionable Hunny, {hunny_name}', value=f'She says, {your_compliment}',
                    inline=False)
    img = random.choice(images)
    embed.set_image(url=img)

    await ctx.send(embed=embed)


@bot.command(name="down")
async def down(ctx):
    print("Left command received")  # Debugging line
    outcome = random.choice(outcomes)

    # Create a base embed
    embed = discord.Embed(color=discord.Color.blue())

    if outcome == "pass":
        embed.title = "Outcome: Pass"
        embed.description = ("You pass through safely.\n\n"
                             "Please choose a new direction\n"
                             "use .left, .right, .up or .down")
        embed.colour = discord.Color.green()
    elif outcome == "blocked":
        embed.title = "Outcome: Blocked"
        embed.description = ("You are blocked by an obstacle.\n\n"
                             "Please choose a new direction\n"
                             "use .left, .right, .up or .down")
        embed.colour = discord.Color.red()
    elif outcome == "trapped":
        embed.title = "Outcome: Trapped"
        embed.description = ("You are trapped and can't move.\n"
                             "use .free to FREE YOURSELF!")
        embed.colour = discord.Color.orange()
    elif outcome == "door":
        embed.title = "Outcome: Door"
        embed.description = "Use .wakeup to help Cod wake up!"
        embed.colour = discord.Color.blue()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1205749795268861962/1243003351306866749/Screenshot_2023-11-01_085038.png?ex=664fe494&is=664e9314&hm=54c7a97972bbd4058c92f0339c57699cfdd185b767a3e2512c4fac8dcb7e4130&")

    # Add additional field and image
    hunny_name = random.choice(names)
    your_compliment = random.choice(compliments)
    embed.add_field(name=f'You run into a fashionable Hunny, {hunny_name}', value=f'She says, {your_compliment}',
                    inline=False)
    img = random.choice(images)
    embed.set_image(url=img)

    await ctx.send(embed=embed)


@bot.command(name="free")
async def free(ctx):
    embed = discord.Embed(title="You have FREED yourself!", color=800080)
    embed.add_field(name="You hear a rumbling in the distance", value="", inline=False)
    embed.set_image(
        url="")
    await ctx.send(embed=embed)
    await asyncio.sleep(5)
    await ctx.invoke(bot.get_command('nightmare'))


@bot.command(name="nightmare")
async def beast(ctx):
    hypnos_names = ["Gromthar", "Brakor", "Tharuk", "Grimnash", "Drak"]
    random_regular_name = random.choice(hypnos_names)
    embed = discord.Embed(title=f'***{random_regular_name}*** has APPEARED!\n'
                                f'***They are a BUNNY KINGDOM MONSTERS!***')
    embed.add_field(name="use .left, .right, .up or .down\n"
                         "to ESCAPE the DANGER!", value="", inline=False)
    image_urls = [
        "https://cdn.discordapp.com/attachments/1205749795268861962/1242284319767007242/nightmare.gif?ex=664d46ee&is=664bf56e&hm=f4e449ef7e8bade84c617dbba2ce005fbbdc605afb33ace299dd57cae66fb9d4&"]
    selected_image_url = random.choice(image_urls)

    # Create an embed and set the image
    embed.set_image(url=selected_image_url)
    await ctx.send(embed=embed)


@bot.command(name='wakeup')
async def collect(ctx):
    random_prize = [""]
    prize = random.choice(random_prize)
    embed = discord.Embed(title="YOU HAVE MADE IT TO CARMEN ELECTRONS DOOR!!\n"
                                "***COD appreciates your HELP!***")
    embed.add_field(name=f'***THANK YOU FOR PLAYING!***', value=f'{prize}', inline=False)
    embed.set_image(
        url="https://cdn.discordapp.com/attachments/1205749795268861962/1243003353152094238/Hunny_1184.png?ex=664fe495&is=664e9315&hm=9189f8887d56b925c73cabe95ebff95681b04966da0f21ceecdfd5d9a52a6a36&")
    await ctx.send(embed=embed)


# Run the bot
token = load_token()
bot.run(token)