import discord
from discord.ext import commands, tasks
from itertools import cycle
import random
import time
import os

#it's your bot's permissions
#Do not change this
intents = discord.Intents.default()
intents.message_content = True

#                      It is your command prefix!
#                                  ⬇
bot = commands.Bot(command_prefix='!', intents=intents)

#Bot status!
status2 = ""

#Don't edit!
blended = ""

#Do not touch!
access = ""

#Information in console(do not touch)
@bot.event
async def on_ready():
    print(f'Logged as: {bot.user}')
    #await bot.change_presence(activity=discord.Status())
    await bot.change_presence(activity=discord.CustomActivity(name=status2 ,emoji='🖥️'))

@bot.command()
async def info(ctx):

    embed = discord.Embed(
        title="Available commands:",
        description=f"**Prefix = '!'  Dostępne komendy: blend5letters, info, ping, permcheck, add_role, mute, unmute, invite, activity, santa**",
        color=0xFF00F6
    )
    await ctx.send(embed=embed)

@bot.command()
async def blend5letters(ctx, word):
    global blended
    for i in range(5):
        blended += random.choice(word)
    await ctx.send(blended)
    blended = ""

@bot.command()
async def activity(ctx, new_activity):
    await bot.change_presence(activity=discord.CustomActivity(name=new_activity))
    embed = discord.Embed(
            title="Success",
            description=f"**Bot's activity has been changed to: {new_activity}!**",
            color=0xFF00F6
        )
    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    bot_latency = round(bot.latency * 1000)
    await ctx.send(f"Pong! {bot_latency} ms.")

@bot.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def permcheck(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Admin")
    if role is None:
        embed = discord.Embed(
            title=f"There is no 'Admin' role!",
            description=f"**You must at first create 'Admin' role!**",
            color=0xFF00F6
        )
        await ctx.send(embed=embed)
        return

    try:
        embed = discord.Embed(
            title="Permcheck result:",
            description=f"**{ctx.author} has permissions**!",
            color=0xFF00F6
        )
        await ctx.send(embed=embed)
    except discord.Forbidden:
        embed = discord.Embed(
            title=f"Error!",
            description=f"**I need have more permissions.**",
            color=0xFF00F6
        )
        await ctx.send(embed=embed)
    except discord.HTTPException as e:
        embed = discord.Embed(
            title=f"Error!",
            description=f"**An error occurred while trying to check {ctx.author} permissions!: {e}**",
            color=0xFF00F6
        )
        await ctx.send(embed=embed)

@bot.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def add_role(ctx, member: discord.Member, getrole):
    # Get the selected role role
    role = discord.utils.get(ctx.guild.roles, name=getrole)
    if role is None:
        embed = discord.Embed(
            title=f"There is no '{role}' role!",
            description=f"**You must at first create {role} role!**",
            color=0xFF00F6
        )
        await ctx.send(embed=embed)
        return

    try:
        # Assign the role to the member
        await member.add_roles(role)
        embed = discord.Embed(
            title="Gived role to player!",
            description=f"**{member}** get role {role} by **{ctx.author}**!",
            color=0xFF00F6
        )
        await ctx.send(embed=embed)
    except discord.Forbidden:
        await ctx.send("I don't have permission to assign roles. Please adjust my permissions.")
    except discord.HTTPException as e:
        await ctx.send(f"An error occurred while trying to give role to the user: {e}")



@bot.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member):
    # Get the Muted role
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if role is None:
        embed = discord.Embed(
            title="There is no 'muted' role!",
            description=f"**You must at first create Muted role!**",
            color=0xFF00F6
        )
        await ctx.send(embed=embed)
        return

    try:
        # Assign the Muted role to the member
        await member.add_roles(role)
        embed = discord.Embed(
            title="User Muted!",
            description=f"**{member}** was muted by **{ctx.author}**!",
            color=0xFF00F6
        )
        await ctx.send(embed=embed)
    except discord.Forbidden:
        await ctx.send("I don't have permission to assign roles. Please adjust my permissions.")
    except discord.HTTPException as e:
        await ctx.send(f"An error occurred while trying to mute the user: {e}")

@bot.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, member: discord.Member):
    # Get the Muted role
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if role is None:
        embed = discord.Embed(
            title="There is no 'muted' role!",
            description=f"**You must at first create Muted role!**",
            color=0xFF00F6
        )
        await ctx.send(embed=embed)
        return

    try:
        # Assign the Muted role to the member
        await member.remove_roles(role)
        embed = discord.Embed(
            title="User Unmuted!",
            description=f"**{member}** was unmuted by **{ctx.author}**!",
            color=0xFF00F6
        )
        await ctx.send(embed=embed)
    except discord.Forbidden:
        await ctx.send("I don't have permission to assign roles. Please adjust my permissions.")
    except discord.HTTPException as e:
        await ctx.send(f"An error occurred while trying to unmute the user: {e}")


@bot.command()
async def invite(ctx):
    embed = discord.Embed(
            title="Invite link",
            description=f"**https://discord.gg/d7wJ4CAebc**",
            color=0xFF00F6
        )
    await ctx.send(embed=embed)

@bot.command()
async def santa(ctx):
    result = random.choice("abcdefghij")
    with open(f'images/{result}.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)




bot.run("your bot's token")
