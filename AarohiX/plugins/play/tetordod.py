import asyncio

import random

from AarohiX import app

from pyrogram.types import (InlineKeyboardButton,

                            InlineKeyboardMarkup, Message)

from strings.filters import command

from pyrogram import filters, Client





txt = [

"يا أجمل من نطق اسمي على لسانه ♡",
"شتبي",
"وش بغيت",
"وش رايك فاللي يناديني بوت ؟ 🦦",
"اسمي فهد ياحب 🙄❤️",
"لبيـه ♥",
"اؤمر شتريد؟❤️🥺",

        ]


        


@app.on_message(command(["بوت","يابوت","bot"]))

async def ktbat(client: Client, message: Message):

      a = random.choice(txt)

      await message.reply(

        f"{a}")
