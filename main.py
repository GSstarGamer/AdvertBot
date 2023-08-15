from aiohttp import web
from discord.ext import commands
import PyUtls as logger
import os
import json
import asyncio


with open('logo.txt', 'r') as f:
    logger.settings.logo = logger.colors.gradientText(
        f.read(), (145, 0, 255), (255, 0, 0), logger.columns())
    logoN = f.read()


logger.settings.logoOnClear = True
logger.settings.centerLogo = True

logger.projectDetails.owner = 'GS'
logger.projectDetails.projectName = 'Auto advert'
logger.projectDetails.version = '0.1'


with open('config.json', 'r') as f:
    config = json.load(f)


async def loadReplit():
    if config['replit247']:
        app = web.Application()

        async def home(request):
            return web.Response(text=logoN+'\nRunning replit 24/7')

        app.router.add_get('/', home)

        def run():
            web.run_app(app, host='0.0.0.0', port=8080)

        def keep_alive():
            try:
                loop = asyncio.get_event_loop()
                loop.create_task(run())
            except:
                pass

        keep_alive()

        try:
            asyncio.get_event_loop().run_forever()
        except KeyboardInterrupt:
            pass
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
    await loadReplit()
    logger.log(
        f'Got channels: {", ".join([channel.name for channel in bot.channels])}')

bot.run(bot.config['token'])
