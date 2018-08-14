import discord
from discord.ext.commands import Bot
import discord.utils



BOT_PREFIX = ('!bren')
bot = Bot(command_prefix=BOT_PREFIX)
tallydict = {}

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('---------')

@bot.command(name='addTally',
                description="Adds a tally",
                brief="git roasted",
                aliases=['tally', 'addtally', 'Addtally'],
                pass_context=True)
async def addTally(ctx, desUser: str, num: int):
    if desUser in tallydict:
        tallydict[desUser] += num
        msg = desUser + ' now has ' + str(tallydict[desUser]) + ' tallies.'
        await ctx.send(msg)
    else:
        tallydict[desUser] = num
        await ctx.send(desUser + ' has recieved their first tally. They now have ' + str(tallydict[desUser]) + ' tallies.')







