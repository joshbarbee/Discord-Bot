import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from datetime import datetime
from bs4 import BeautifulSoup
import urllib3
import urllib.parse
import urllib.request
import random


Client = discord.Client()
bot_prefix= "!"
client = commands.Bot(command_prefix=bot_prefix)
while True:
    queue_members = []
    @client.event
    async def on_ready():
        print("Bot Online!")
        print("Name: {}".format(client.user.name))
        print("ID: {}".format(client.user.id))

    @client.command(pass_context=True)
    async def date(ctx):
        currentdate = datetime.now().strftime("%B %d, %Y")
        await client.say(currentdate)
    
    @client.command(pass_context=True)
    async def connect(ctx):
        if client.is_voice_connected(ctx.message.server):
            return await client.say("I am already connected to a voice channel. Do not disconnect me if I am in use!")
        author = ctx.message.author
        voice_channel = author.voice_channel
        vc = await client.join_voice_channel(voice_channel)
    
    @client.command(pass_context=True)
    async def queue(ctx):
        await client.say("%s started a queue Type !join to join them" % ctx.message.author.name)
        queue_members.append(ctx.message.author.name)
    @client.command(pass_context=True)
    async def join(ctx):
        
        
        if ctx.message.author.name not in queue_members:
            queue_members.append(ctx.message.author.name) 
            await client.say("%s joined the queue." % ctx.message.author.name)
            await client.say("Currently in queue: ")
            for item in queue_members:
                await client.say(str(item))
        elif len(queue_members) > 5:
            await client.say("Too many queue members")
        else:
            await client.say("Currently in queue: ")
            for item in queue_members:
                await client.say(str(item))
   
    @client.command(pass_context = True)
    async def disconnect(ctx):
        for x in client.voice_clients:
            if(x.server == ctx.message.server):
                return await x.disconnect()

    @client.command(pass_context=True)
    async def commands(ctx):
        await client.say("@%s My commands are:" % ctx.message.author.name)
        await client.say("`date`")
        await client.say("`connect`")
        await client.say("`queue`")
        await client.say("`join`")
        await client.say("`youtube`")
    
    @client.command(pass_context=True)    
    async def youtube(ctx):
        link_list = []
        text_to_search = ctx.message.content.replace('!youtube', '')
        query = urllib.parse.quote(text_to_search)
        url = "https://www.youtube.com/results?search_query=" + query
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")
        for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
                link_list.append('https://www.youtube.com' + vid['href'])
        await client.say(link_list[0])
    @client.command(pass_context=True)
    async def 8ball(ctx):
        8balloptions = ["Not so sure", "42", "Most likely", "Absolutely not", "Outlook is good", "I see good things happening", "Never",
"Negative", "Could be", "Unclear, ask again", "Yes", "No", "Possible, but not probable"]
        await client.say("@%s. The magic 8 ball says "+random.choice(8balloptions) %ctx.message.author.name)
    client.run("")
