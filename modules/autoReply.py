from discord.ext import commands
import discord
import PyUtls as logger
import asyncio


class autoReplyCog(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot
        self.config = self.bot.config
        self.enabled = self.config['autoReply']['enabled']
        self.messageToSend = self.config['autoReply']['autoReplyMessage']

    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    @commands.Cog.listener()
    async def on_message(self, ctx: commands.Context) -> None:
        if self.enabled and isinstance(ctx.channel, discord.channel.DMChannel) and ctx.author != self.bot.user:
            async with ctx.channel.typing():
                logger.log(f'Auto reply: {ctx.author.name} - {ctx.content}')
                await asyncio.sleep(1)
                await ctx.reply(self.messageToSend)

    @commands.command(alias=['autoreply'])
    async def autoReply(self, ctx: commands.Context, option: bool) -> None:
        if self.enabled != option:
            self.enabled = option
            await ctx.message.edit(f'Auto reply set to {option}')

        else:
            await ctx.message.edit(f'Auto reply is already set to {option}')


async def setup(bot: commands.Bot):
    await bot.add_cog(autoReplyCog(bot))
