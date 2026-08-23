import os
from flask import Flask
from threading import Thread
import discord
from discord.ext import commands

# 網頁伺服器：用來騙過 Render 不讓它關機
app = Flask('')
@app.route('/')
def home():
    return "機器人 24 小時完全免費運作中！"
def run():
    app.run(host='0.0.0.0', port=8080)
def keep_alive():
    t = Thread(target=run)
    t.start()

# 機器人設定
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'【免費啟動成功】機器人 {bot.user} 已上線！')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == "你好":
        await message.channel.send(f"嗨！{message.author.mention}，這是一個完全免費的 24 小時機器人！")

keep_alive()
bot.run(os.getenv('DISCORD_TOKEN')) # 安全讀取環境變數

