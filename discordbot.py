# -*- coding: utf-8 -*-

# ライブラリのインポート
import discord
import asyncio

#bot = commands.Bot(command_prefix='/')
TOKEN = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

# ボットの起動時に実行されるイベントハンドラを定義
@client.event
async def on_ready():
    print('Bot Launched')

# メッセージの送信時に実行されるイベントハンドラを定義
@client.event
async def on_message(message):
    if message.author.bot:
        pass
    elif message.content.startswith('こんにちは！'):
        send_message = f'{message.author.mention}さん、こんにちは！'
        await message.channel.send(send_message)

#ボットを実行
client.run(TOKEN)
#ここより下に書かれた処理はボットが停止するまで実行されない

bot.run(token)
