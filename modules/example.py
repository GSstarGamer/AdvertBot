from discord.ext import commands


class example(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot

    # @commands.Cog.listener()
    # async def on_ready(self) -> None:
    #     pass

    @commands.command(hidden=True)
    async def command(self, ctx: commands.Context) -> None:
        pass


async def setup(bot: commands.Bot):
    await bot.add_cog(example(bot))
