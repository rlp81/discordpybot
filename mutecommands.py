import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import asnycio

Client = commands.Bot(command_prefix="!", halp_commmand =None)

@Client.command(name="Mute")
@has_permissions(administrator=True)
async def mute(context, member: discord.Member = None, reason = None):
    if reason == None:
        await context.send("You need a reason to mute them!")
    if not reason == None:
        if member == None:
            await context.send("You need to mention someone to mute!")
        if not member == None:
            guild = context.guild
            muterole = discord.utils.get(guild.roles, name="Muted")
            if not muterole:
                muterole = await guild.create_role(name="Muted")
                for channel in guild.channels:
                    await channel.set_permissions(muterole, speak=False, send_messages=False)
            await member.add_roles(muterole)
            await context.send(f"I muted {member.display_name} for {reason}")
            await member.send(f"You were muted for {reason}")

@Client.command(name="UnMute")
@has_permissions(administrator=True)
async def unmute(context, member: discord.Member = None):
    if member == None:
        await context.send("You need to mention someone to unmute!")
    if not member == None:
        guild = context.guild
        muterole = discord.utils.get(guild.roles, name="Muted")
        if not muterole:
            muterole = await guild.create_role(name="Muted")
            for channel in guild.channels:
                await channel.set_permissions(muterole, speak=False, send_messages=False)
        await member.remove_roles(muterole)
        await context.send(f"I unmuted {member.display_name}.")
        await member.send(f"You have been unmuted by, {member.display_name}.")

@Client.command(name="tempmute", aliases=["TempMute", "Tempmute", "tmute", "Tmute"])
@has_permissions(manage_roles=True)
async def Tmute(context, message, member: discord.Member, *, message2):
    guild = context.guild
    time = int(message)
    reason = message2
    mutedrole = discord.utils.get(guild.roles, name="Muted")
    if not mutedrole:
        mutedrole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedrole, speak = False, send_messages = False)
    await member.add_roles(mutedrole)
    await context.send(f"I muted {member.mention} for {reason}")
    await member.send(f"You were muted in {guild.name} for {reason} by {context.author}")
    await asyncio.sleep(time)
    await member.remove_roles(mutedrole)
    await context.send(f"I have unmuted {member.mention} because it has been {time} minutes.")
    await member.send(f"You have been unmuted in {guild.name}.")
@Client.event
async def on_ready():
  print("Bot is ready!")
Client.run("ODM4NDUxMjA1NjIwNDk4NDMy.YI7SiQ.ApqCLytQ02Pb0LjxIReIgEjSPk4")
