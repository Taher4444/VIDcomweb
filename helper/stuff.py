#    This file is part of the CompressorBot distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in < https://github.com/wahebtalal/VideoCompressBot/blob/main/License> .

from .worker import *


async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"🌋Pɪɴɢ = {ms}ms"
    await event.reply(v + "\n" + p)


async def start(event):
    ok = await event.client(GetFullUserRequest(event.sender_id))
    await event.reply(
        f"اهلا `{ok.user.first_name}`\nهذا بوت ضغط الفيديو.\nيقوم بتقليص حجم الفيديو مع الحفاظ على دقته.\nتستطيع انشاء لقطات شاشة\عينة للفيديو.",
        buttons=[
            [Button.inline("مساعدة", data="ihelp")],
            [
                Button.url("السورس كود", url="github.com/wahebtalal/VideoCompressBot"),
                Button.url("المطور", url="t.me/Wahiebtalal"),
            ],
        ],
    )


async def help(event):
    await event.reply(
        "**🐠 بوت ضغط الفيديو**\n\n+يقوم هذا البوت بضغط مقاطع الفيديو مع تغيير ضئيل في الجودة.\n+انشاء عينة فيديو مضغوط\n+سهل الاستخدام\n-نظرًا لإعدادات الجودة ، يستغرق البوت وقتًا في الضغط.\nلذا كن صبورًا وأرسل مقاطع الفيديو واحدًا تلو الآخر بعد الانتهاء.\nلا تقم بارسال رسائل عشوائية لتجنب الحظر.\n\nفقط قم بإعادة توجيه الفيديو"
                      )


async def ihelp(event):
    await event.edit(
        "**🐠 بوت ضغط الفيديو**\n\n+يقوم هذا البوت بضغط مقاطع الفيديو مع تغيير ضئيل في الجودة.\n+انشاء عينة فيديو مضغوط\n+سهل الاستخدام\n-نظرًا لإعدادات الجودة ، يستغرق البوت وقتًا في الضغط.\nلذا كن صبورًا وأرسل مقاطع الفيديو واحدًا تلو الآخر بعد الانتهاء.\nلا تقم بارسال رسائل عشوائية لتجنب الحظر.\n\nفقط قم بإعادة توجيه الفيديو",
        buttons=[Button.inline("رجوع", data="beck")],
    )


async def beck(event):
    ok = await event.client(GetFullUserRequest(event.sender_id))
    await event.edit(
        f"اهلا `{ok.user.first_name}`\nهذا بوت ضغط الفيديو.\nيقوم بتقليص حجم الفيديو مع الحفاظ على دقته.\nتستطيع انشاء لقطات شاشة\عينة للفيديو.",
             buttons=[
            [Button.inline("مساعدة", data="ihelp")],
            [
                Button.url("السورس كود", url="github.com/wahebtalal/VideoCompressBot"),
                Button.url("المطور", url="t.me/Wahiebtalal"),
            ],
        ],
    )


async def sencc(e):
    key = e.pattern_match.group(1).decode("UTF-8")
    await e.edit(
        "اختر الطريقة",
        buttons=[
            [
                Button.inline("الافتراضي", data=f"encc{key}"),
                Button.inline("تخصيص", data=f"ccom{key}"),
            ],
            [Button.inline("رجوع", data=f"back{key}")],
        ],
    )


async def back(e):
    key = e.pattern_match.group(1).decode("UTF-8")
    await e.edit(
        "🐠  **ماذا تريد** 🐠",
        buttons=[
            [
                Button.inline("إنشاء عينة ", data=f"gsmpl{key}"),
                Button.inline("لقطات الشاشة ", data=f"sshot{key}"),
            ],
            [Button.inline("ضغط", data=f"sencc{key}")],
        ],
    )


async def ccom(e):
    await e.edit("أرسل اسم للملف ")
    wah = e.pattern_match.group(1).decode("UTF-8")
    wh = decode(wah)
    out, dl, thum, dtime = wh.split(";")
    chat = e.sender_id
    async with e.client.conversation(chat) as cv:
        reply = cv.wait_event(events.NewMessage(from_users=chat))
        repl = await reply
        if "." in repl.text:
            q = repl.text.split(".")[-1]
            g = repl.text.replace(q, "mkv")
        else:
            g = repl.text + ".mkv"
        outt = f"encode/{chat}/{g}"
        x = await repl.reply(
            f"اسم الملف : {g}\n\nإرسال صورة مصغرة  Thumbnail ."
        )
        replyy = cv.wait_event(events.NewMessage(from_users=chat))
        rep = await replyy
        if rep.media:
            tb = await e.client.download_media(rep.media, f"thumb/{chat}.jpg")
        elif rep.text and not (rep.text).startswith("/"):
            url = rep.text
            os.system(f"wget {url}")
            tb = url.replace("https://telegra.ph/file/", "")
        else:
            tb = thum
        omk = await rep.reply(f"Thumbnail {tb} Setted Successfully")
        hehe = f"{outt};{dl};{tb};{dtime}"
        key = code(hehe)
        await customenc(omk, key)
