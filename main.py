import discord
from discord.ext import commands
from model import get_class
intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command("helpme")
async def helpme(ctx):
    await ctx.send(f'Привет!Я бот по истории!\nЯ помогу тебе с богами Древнего Египта.')

@bot.command("check")
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file = attachment.filename
            await attachment.save(f'./{file}')
            x = get_class(model_path="./keras_model.h5" , labels_path="./labels.txt", image_path = f'./{file}')
            await ctx.send(x)

bot.run("")
