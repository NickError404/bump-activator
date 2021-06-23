import discord
from discord import message
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix="$s", case_insentitive=True)


@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.idle,
        activity=discord.Game("Developer by Nı¢κ \n My DC: Nı¢κ#5562"))
    print('O {0.user} está online e funcionando nos conformes.'.format(client))


@client.command()
async def bump_activeD5032C(ctx):
    while (True):
        await ctx.send(
            '**Olá cavalheiros, gostaria de avisar que já é momendo te dar o comando ```!d bump```em #:computer:・comandos , alguém por obséquio poderia me ajudar?**'
        )
        await asyncio.sleep(7200)


client.run('ODU3MDY4Nzc5NDE5MDc0NjAy.YNKNgA.jRL7f9xQ32O0hZb0f8sFvvaAkIk')
