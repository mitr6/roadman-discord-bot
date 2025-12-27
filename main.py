import discord
from discord.ext import commands
import datetime
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="roadman, ", intents=intents, help_command=None)

bot.start_time = datetime.datetime.utcnow()
last_message = {} # Dictionary to store deleted messages per channel

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    await bot.change_presence(activity=discord.Game(name="roadman, help"))

@bot.event
async def on_message_delete(message):
    if message.author.bot:
        return
    last_message[message.channel.id] = {
        "content": message.content,
        "author": message.author.name,
        "avatar": message.author.display_avatar.url
    }


@bot.command()
async def dsay(ctx):
    """Shows the last deleted message in the channel."""
    data = last_message.get(ctx.channel.id)
    if not data:
        return await ctx.send("There are no deleted messages to show!")
    
    embed = discord.Embed(description=data["content"], color=0xe67e22)
    embed.set_author(name=data["author"], icon_url=data["avatar"])
    embed.set_footer(text="Deleted message recovered")
    await ctx.send(embed=embed)

@bot.command()
async def snipe(ctx):
    """Alias for dsay since they are often used interchangeably."""
    await dsay(ctx)

@bot.command()
async def ping(ctx):
    await ctx.send(f"🏓 Pong! {round(bot.latency * 1000)}ms")

@bot.command()
async def uptime(ctx):
    now = datetime.datetime.utcnow()
    diff = now - bot.start_time
    await ctx.send(f"Bot Uptime: `{str(diff).split('.')[0]}`")

@bot.command()
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    await ctx.send(member.display_avatar.url)

@bot.command()
async def botinfo(ctx):
    embed = discord.Embed(title="Bot Information", color=0x3498db)
    embed.add_field(name="Library", value="Discord.py")
    embed.add_field(name="Servers", value=len(bot.guilds))
    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="No reason provided"):
    await member.kick(reason=reason)
    await ctx.send(f"✅ **{member}** has been kicked | {reason}")

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="No reason provided"):
    await member.ban(reason=reason)
    await ctx.send(f"🔨 **{member}** has been banned | {reason}")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    msg = await ctx.send(f"🗑️ Deleted `{amount}` messages.")
    await asyncio.sleep(3)
    await msg.delete()

@bot.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member):
    # This assumes you have a role named 'Muted'
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
    await ctx.send(f"🔇 {member.mention} has been muted.")


@bot.command()
async def join(ctx):
    if not ctx.author.voice:
        return await ctx.send("Join a voice channel first!")
    await ctx.author.voice.channel.connect()
    await ctx.send("Connected to voice!")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("Disconnected.")

@bot.command()
async def play(ctx, url):
    await ctx.send(f"🎵 Now playing: {url} (Basic implementation)")
    # Music logic requires yt-dlp/FFmpeg setup; this is the command trigger.


@bot.command()
async def help(ctx, category=None):
    if not category:
        embed = discord.Embed(color=0xe67e22)
        embed.set_author(name="Comenzi", icon_url=bot.user.display_avatar.url)
        embed.set_thumbnail(url=bot.user.display_avatar.url)
        embed.add_field(name="Moderare", value="`roadman, help moderation`", inline=False)
        embed.add_field(name="Altele", value="`roadman, help others`", inline=False)
        await ctx.send(embed=embed)
    elif category.lower() == "moderation":
        await ctx.send("**Moderation:** kick, ban, mute, unmute, purge, lock, unlock")
    elif category.lower() == "others":
        await ctx.send("**Others:** avatar, botinfo, ping, uptime, snipe, dsay, serverinfo")

bot.run('YOUR_TOKEN_HERE')