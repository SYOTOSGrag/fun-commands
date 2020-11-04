# just some imports
import discord
from discord.ext import commands

# separating them into groups depending on the commands
import random

import math
from math import sqrt

# ill be using client instead of bot because it seems easier for me to understand
client = commands.Bot(command_prefix = "!", case_insensitive = True)
# you can add a whole bunch of other stuffs if you want ^^^

@client.event
async def on_ready():
    print("SYOTOS is online\n-----")
    activity=discord.Activity(type=discord.ActivityType.watching, name="Hey, use `t;help` for further information")
	# if you want to add a status or activity use the format I used if you want
    await client.change_presence(status = discord.Status.idle, activity=activity)
	
@client.command(name='8ball', description='Ask the 8ball a question', usage='<question>')
async def _8ball(ctx, *, message=None):
	# this is basically a list of the responses you might see in an 8ball
	response = ['It is certain',
                'It is decidedly so',
                'Without a doubt',
                'Yes – definitely',
                'You may rely on it',
                'As I see it, yes',
                'Most likely',
                'Outlook good',
                'Yes Signs point to yes',
                'Reply hazy',
                'try again',
                'Ask again later',
				'Better not tell you now',
				'Cannot predict now',
				'Concentrate and ask again',
				"Don't count on it",
				'My reply is no',
				'My sources say no',
				'Outlook not so good',
				'Very doubtful'
                ]
	# if you dont ask a question, then it will send this
    if message is None:
		# regular text, no embeds
        await ctx.send("Please ask a question")
    else:
		# this will delete the question you ask
        await ctx.message.delete()
		# using embed messages
        embed = discord.Embed(title='**8ball**', colour=discord.Colour(0x000000), inline=False)
        embed.add_field(name="Question", value=f'```{message}```', inline=False)
        embed.add_field(name="Answer", value=f'```{random.choice(response)}```', inline=False)
        await ctx.send(embed=embed)	

# your token
..
client.run("TOKEN")
