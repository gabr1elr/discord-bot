import time
import random
import discord
from discord.ext.commands import Bot
from discord.utils import get
from discord.ext import commands
import asyncio

Client = discord.Client()
client = commands.Bot(command_prefix = "/?")


chat_filter = ["JERK"]
bypass_list = []

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="/?help", type = 3))
    print("Bot is ready.")

@client.event
async def on_message(message):
    if message.content.upper().startswith('/?HELP'):
        embed = discord.Embed(title="Commands list", description="You got here using /?help", color=0x0404B4)
        embed.add_field(name="Command 1", value="/?info - see a documentation about Python.", inline=False)
        embed.add_field(name="Command 2", value="/?sendtts - send a TTS message.", inline=False)
        embed.add_field(name="Command 3", value="/?cool - comanda distractiva.", inline=False)
        embed.add_field(name="Command 4", value="/?tableflip", inline=False)
        embed.add_field(name="Command 5", value="/?shrug", inline=False)
        embed.add_field(name="Command 6", value="/?unflip", inline=False)
        embed.add_field(name="Command 7", value="/?zalgo", inline=False)
        embed.add_field(name="Command 8", value="/?thinking", inline=False)
        embed.add_field(name="Command 9", value="/?invitebot - link for bot to join your discord server.", inline=False)
        embed.add_field(name="Command 10", value="/?say - you make the bot say something", inline=False)
        embed.add_field(name="Command 11", value="/?sayd - same as /?say but deletes your message.", inline=False)
        embed.add_field(name="Command 12", value="/?ping - pong.", inline=False)
        embed.add_field(name="Command 13", value="/?credits - see the bot owner.", inline=False)
        await client.send_message(message.channel, embed=embed)
    if message.content.startswith('/?info'):
        await client.send_message(message.channel, "https://discordpy.readthedocs.io/en/latest/api.html#discord.Client.user%22")
    if message.content.upper().startswith('/?SENDTTS'):
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])), tts=True)
        return
    if message.content.upper().startswith ('/?CREDITS'):
        await client.send_message(message.channel, "dorttog is the owner of this discord bot.")  
    if message.content.startswith("/?cool"):
        await client.send_message(message.channel, 'Who is cool? Type /?name @name')

        def check(msg):
            return msg.content.startswith('/?name')

        message = await client.wait_for_message(author=message.author, check=check)
        name = message.content[len('/?name'):].strip()
        await client.send_message(message.channel, '{} is cool.'.format(name))
    if message.content.upper().startswith ('/?TABLEFLIP'):
        await client.send_message(message.channel, "(╯°□°）╯︵ ┻━┻")
    if message.content.upper().startswith ('/?SHRUG'):
        await client.send_message(message.channel, "¯\_(ツ)_/¯")
    if message.content.upper().startswith ('/?UNFLIP'):
        await client.send_message(message.channel, "┬─┬ ノ( ゜-゜ノ)")
    if message.content.upper().startswith ('/?ZALGO'):
        await client.send_message(message.channel, "z̛͋̚ǎ̐̀l̛̅͠g̀͐͘ơ̋͝")    
    if message.content.upper().startswith ('/?THINKING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> is thinking :thinking:." % (userID))
    if message.content.upper().startswith('/?INVITEBOT'):
        await client.send_message(message.channel, "LINK INVITATIE BOT")
    if message.content.upper().startswith('/?SAYD'):
        args = message.content.split(" ")
        await client.delete_message(message)
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        return
    if message.content.upper().startswith('/?SAY'):
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
    if message.content.upper().startswith('/?PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    contents = message.content.split(" ") #contents is a list type
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                await client.delete_message(message)
                await client.send_message(message.channel, "You aren't allowed to type that word here!")

client.run("BOT TOKEN")

