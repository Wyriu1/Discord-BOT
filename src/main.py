import random
import os

from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 295229319309950977  # Change to your discord id

listOfFunBanReason = ["Aucune raison",
                      "Et ça fait tik tak boom",
                      "Ca fait bim et ça fait boom",
                      "La sentence est irrévocable"]
@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

# Interesting ressources :
# - https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#context
# -
# Task 1: Reply with the user's name
@bot.command()
async def name(ctx):
    author = ctx.author
    await ctx.send(f"Your name is {author}")


# Task 2: Roll a 6-sided die
@bot.command()
async def d6(ctx):
    roll = random.randint(1, 6)
    await ctx.send(f"You rolled a {roll}")


# Task 3: Respond to "Salut tout le monde"
@bot.event
async def on_message(message):
    if message.content.lower() == "salut tout le monde":
        author = message.author
        await message.channel.send(f"Salut tout seul, {author.mention}")
    await bot.process_commands(message)

# Task 4 : Give admin role to user
@bot.command()
async def admin(ctx, member: discord.Member):
    # await ctx.send(f"{member.name}")
    guild = ctx.guild
    admin_role = discord.utils.get(guild.roles, name="Admin")

    if not admin_role:
        admin_role = await guild.create_role(name="Admin", permissions=discord.Permissions.all())

    await member.add_roles(admin_role)
    await ctx.send(f"Role admin given to {member.mention}")

#Task 5 : Ban member
@bot.command()
async def ban(ctx, member: discord.Member, reason=None):
    # Get a random reason if none is given from listOfFunBanReason
    if reason is None:
        reason = random.choice(listOfFunBanReason)
    await member.ban(reason=reason)
    await ctx.send(f"{member.mention} has been banned for the following reason: {reason}")



print(DISCORD_TOKEN)
token = DISCORD_TOKEN
bot.run(token)  # Starts the bot