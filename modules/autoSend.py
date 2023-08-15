from discord.ext import commands, tasks
import datetime
import discord
import threading
import requests as req
import PyUtls as logger
import asyncio

onCooldown = []


class TemporaryItem:
    def __init__(self, lifetime_seconds, data, item_list):
        self.data = data
        self.item_list = item_list
        self.timer = threading.Timer(lifetime_seconds, self._expire)
        self.timer.start()
        self.item_list.append(self)

    def _expire(self):
        self.item_list.remove(self)


def isonCooldown(data):
    global onCooldown

    for item in onCooldown:
        if item.data == data:
            return True
    return False


def addCooldownChannel(channelID, lifetime_seconds):
    global onCooldown
    TemporaryItem(lifetime_seconds, channelID, onCooldown)


def getMessage(path):
    with open(path, 'r') as f:
        return f.read()


async def sendMessage(message, channel, token):
    global onCooldown
    channelID = channel.id
    if not isonCooldown(channelID):
        headers = {
            'authorization': token,
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        }
        json_data = {
            'content': message,
            'tts': False,
            'flags': 0,
        }
        response = req.post(
            f'https://discord.com/api/v9/channels/{channelID}/messages',
            headers=headers,
            json=json_data,
        )
        status_code = response.status_code
        response = response.json()
        if status_code != 200:
            if response['message'] == 'This action cannot be performed due to slowmode rate limit':
                addCooldownChannel(channelID, response['retry_after'])
                logger.fail(f'{channel.name} on cooldown, 1')
            elif response['message'] == 'Missing Permissions':
                logger.fail(f'{channel.name} no perms, Removing')
                return 'remove'
            else:
                logger.error(response)
        else:
            logger.success(f'Sent in {channel.name}')
    else:
        logger.fail(f'{channel.name} on cooldown, 2')


class autoSendCog(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot
        self.channels = self.bot.channels
        self.config = self.bot.config

        @tasks.loop(seconds=self.config["loopDelay"]['seconds'], minutes=self.config["loopDelay"]['minutes'], hours=self.config["loopDelay"]['hours'])
        async def mainLoop():
            if len(self.channels) == 0:
                logger.fail('No channels, Exiting')
                mainLoop.stop()
                exit()
            for channel in self.channels:
                if self.bot.get_channel(channel.id):
                    msg = getMessage(self.config['messagePath'])
                    response = await sendMessage(msg, channel, self.config['token'])
                    if response == 'remove':
                        self.channels.remove(channel)
                    await asyncio.sleep(self.config['itterDelay'])
                else:
                    self.channels.remove(channel)
                    logger.fail(f'Channel non existant, Removed')
        mainLoop.start()

    # @commands.Cog.listener()
    # async def on_ready(self) -> None:
    #     pass
    # @commands.command(hidden=True)
    # async def command(self, ctx: commands.Context) -> None:
    #     pass


async def setup(bot: commands.Bot):
    await bot.add_cog(autoSendCog(bot))
