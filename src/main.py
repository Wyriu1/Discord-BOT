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


token = "MTE2Njc4OTY4ODQwNTc4Njc2NQ.Gsbof3.JopWLZOYcht2yEGusdBhIeyn5EiGIgbge1oIvM"
bot.run(token)  # Starts the bot