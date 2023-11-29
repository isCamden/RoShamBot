import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="", intents=intents)

def determine_winner(player_choice, bot_choice):
    if (
        (player_choice == 'rock' and bot_choice == 'scissors') or
        (player_choice == 'paper' and bot_choice == 'rock') or
        (player_choice == 'scissors' and bot_choice == 'paper')
    ):
        return "You win"
    else:
        return "I win"

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.change_presence(activity=discord.Game(name="Rock, Paper, Scissors!"))

@bot.event
async def on_message(message):
    if message.author != bot.user:
        if message.content.startswith('!rps'):
            choices = ['rock', 'paper', 'scissors']
            user_choice = message.content.split(' ')[1].lower() if len(message.content.split(' ')) > 1 else None
            if user_choice not in choices:
                await message.channel.send("Invalid choice! Choose 'rock', 'paper', or 'scissors'.")
                return
            bot_choice = random.choice(choices)
            result = "It's a tie" if user_choice == bot_choice else determine_winner(user_choice, bot_choice)
            await message.channel.send(f"You chose {user_choice}, I chose {bot_choice}. {result}!")

        else:
            response_message = None

        if response_message is not None:
            await message.channel.send(response_message)

    await bot.process_commands(message)

bot.run("YOUR_BOT_TOKEN") #replace with token before use