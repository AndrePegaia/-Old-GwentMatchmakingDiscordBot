from discord.ext import commands

mensagemErro = True

class Default(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, ex):
        if mensagemErro == True:
            await ctx.send(':rotating_light: :rotating_light:  Erro detectado!!  :rotating_light: :rotating_light:')
            await ctx.send("Por favor cheque como utilizar o comando corretamente digitando =help. Em caso de dúvida, entre em contato com o administrador.")
            await ctx.send(ex)

    @commands.command(aliases=['clear', 'limpar'], brief='Apaga mensagens recentes', description='Deleta a quantidade de mensagens especificada')
    async def clean(self, ctx, arg):
        await ctx.channel.purge(limit=int(arg) + 1)


def setup(bot):
    bot.add_cog(Default(bot))
