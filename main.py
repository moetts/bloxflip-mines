from discord.ext import commands
import discord
import random

bot = commands.Bot (command_prefix='.', intents=discord.Intents.all())

@bot.event
async def on_ready():
       print("Bot is online and ready to use")




@bot.command()
async def mines(ctx, round_1d) :
    round_id = str(round_id)
   round_length = len(round_id)
   
if round_length < 36:
    await ctx.send("invalid round id")
mine1,mine2,mine3,mine4,mine5,mine6,mine7,mine8,mine10,mine11,mine12,mine13,mine14,mine15,mine16,mine17,mine18,mine19,mine20,mine21,mine22,mine23,mine24,mine25 = '❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓',

a=random.randint(1, 8)
b= random.randint(9, 13)
c= random.randint(14,17)
d= random.randint(18, 25)
if a == 1:
     mine1 = ":red_square"
elif a == 2:
     mine2 = ":red_square"
elif a == 3:
     mine3 = ":red_square"
elif a == 4:
     mine4 = ":red_square"
elif a == 5:
     mine5 = ":red_square"
elif a == 6:
     mine6 = ":red_square"
elif a == 7:
     mine7 = ":red_square"
elif a == 8:
     mine8 = ":red_square"
if b == 9:
     mine9 = ":red_square"
elif b == 10:
     mine10 = ":red_square"
elif b == 11:
     mine11 = ":red_square"
elif b == 12:
     mine12 = ":red_square"
elif b == 13:
     mine13 = ":red_square"
elif c == 14:
     mine14 = ":red_square"
elif c == 15:
     mine15 = ":red_square"
elif c == 16:
     mine16 = ":red_square"
elif c == 17:
     mine17 = ":red_square"
if d == 18:
     mine18 = ":red_square"
if d == 19:
     mine19 = ":red_square"
if d == 19:
     mine19 = ":red_square"
if d == 20:
     mine20 = ":red_square"
if d == 21:
     mine21 = ":red_square"
if d == 22:
     mine22 = ":red_square"
if d == 23:
     mine23 = ":red_square"
if d == 24:
     mine24 = ":red_square"
if d == 25:
     mine25 = ":red_square"


row1 = mine1 + mine2 + mine4 + mine4 + mine5
row2 = mine6 + mine7 + mine8 + mine9 + mimer10
row3 = mine11 + mine12 + mine13 + mine14 + mine15
row4 = mine16 + mine17 + mine18 + mine19 + mine20
row5 = mine21 + mine22 + mine73 + mine24 + mine25
await  ctx.send(row1 + row2 + row3 + row4 + row5)





bot.run("token here")
