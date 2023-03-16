import discord
from discord.ext import commands
import load_json_variable as variable

prefix = "!"
bot = commands.Bot(command_prefix=prefix,intents=discord.Intents.all())

discord_token = "MTA4NTM0MjMwNDgyODY2NTg4Ng.GZxSr3.N6rL5NKUaerSCvyXVPJcfkfZ42WRRlXKBrZ_eY" # 추후에 꼭 숨길것


@bot.event
async def on_ready():
    print("we have logged in as {}".format(bot))
    print("bot name {}" .format(bot.user.name))
    print("Bot ID {}" .format(bot.user.id))

@bot.event
async def on_message(message):
    if message.author.bot:
        return None
    else :
        await bot.process_commands(message)

@bot.command(name = "도움")
async def test(ctx):
    await ctx.send("```도움말 표시 : !도움\n\n채널 생성 방법 : !채널생성 \"강의종류(교양, 전공 등)\"  \"강의명\"  \"분반이 있는경우 몇 분반인지 기제\" (띄어쓰기가 없을경우 \"\" 생략 가능) \n e.g. !채널생성 교양 \"자기탐색과 성장비젼\" 105반```")


# @bot.command(name = "채널생성")
# async def test(ctx, *args):
#     guild = ctx.message.guild
#     arguments = ', '.join(args)
#     arg = arguments.split(",")
#     arg_1 = arg[0]
#     arg_2 = arg[1]
#     if(len(arg) == 3):
#         arg_3 = arg[2]
#     print(arguments)
#     if (arg_1 == "전공"):
#         category = discord.utils.get(guild.categories, name = "전공")
#     elif (arg_1 == "교양"):
#         category = discord.utils.get(guild.categories, name = "교양")

#     await guild.create_text_channel(arg_2, category = category)

@bot.command(name = "test")
async def test(ctx):
    guild = ctx.message.guild
    channel = discord.utils.get(guild.text_channels)
    print(channel)

bot.run(variable.get_token())
