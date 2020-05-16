import time

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

temp = 'p9Bpw.7auvDg4AcIINwrDwz7JfT4nZ13Y'

@bot.event
async def on_ready():
    print('Done')

@bot.command()
async def dt(ctx):
	embed = discord.Embed(
		title = 'Date and time',
		description = time.ctime(),
		colour = discord.Colour.gold()
	)
	author = 'MS#4438'
	await ctx.channel.send(embed=embed)






bot.run('NzAxOTE1MTE1MjIxNDE4MDA1.X' + temp)
