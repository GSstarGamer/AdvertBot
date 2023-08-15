import discord
from discord.ext import commands, tasks
import PyUtls as logger
import os
import json
import asyncio


with open('logo.txt', 'r') as f:
    logger.settings.logo = logger.colors.gradientText(
        f.read(), (145, 0, 255), (255, 0, 0), logger.columns())


logger.settings.logoOnClear = True
logger.settings.centerLogo = True

logger.projectDetails.owner = 'GS'
logger.projectDetails.projectName = 'Auto advert'
logger.projectDetails.version = '0.1'


with open('config.json', 'r') as f:
    config = json.load(f)

logger.startUp(False)
bot = commands.Bot(command_prefix=config['prefix'],
                   help_command=None, self_bot=True)

bot.config = config


async def load_modules():
    for module in os.listdir('modules'):
        if module.endswith('.py') and module != 'example.py':
            try:
                await bot.load_extension(f'modules.{module[:-3]}')
            except Exception as e:
                logger.fail(e)


@bot.event
async def on_ready():
    bot.channels = []
    for channel in bot.config['channels']:
        check = bot.get_channel(channel)
        if check:
            bot.channels.append(check)
        else:
            logger.error(f'{channel} is invalid')

    with open(config['messagePath'], 'r') as f:
        messageToSend = f.read()
        if messageToSend == '' or messageToSend == ' ':
            logger.error(f'No message in "{config["messagePath"]}"')
            exit()

    await load_modules()
    logger.success(f'Ready, Logged as {bot.user.name}')
    logger.log(
        f'Got channels: {", ".join([channel.name for channel in bot.channels])}')

bot.run(bot.config['token'])
