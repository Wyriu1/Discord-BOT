import random

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

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

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


token = "MTE2Njc4OTY4ODQwNTc4Njc2NQ.Gsbof3.JopWLZOYcht2yEGusdBhIeyn5EiGIgbge1oIvM"
bot.run(token)  # Starts the bot