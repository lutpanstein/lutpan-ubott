# Ported by X_ImFine
# Recode by @mrismanaziz

from telethon.tl.functions.contacts import BlockRequest, UnblockRequest

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, DEVS
from userbot.events import register
from userbot.utils import get_user_from_event, man_cmd


@man_cmd(pattern="gkick(?: |$)(.*)")
@register(pattern=r"^\.cgkick(?: |$)(.*)", sudo=True)
async def gspide(rk):
    lazy = rk
    sender = await lazy.get_sender()
    me = await lazy.client.get_me()
    if sender.id != me.id:
        rkp = await lazy.reply("`Processing...`")
    else:
        rkp = await lazy.edit("`Processing...`")
    me = await rk.client.get_me()
    await rkp.edit("`LAGI NGEKICK NI MAKHLUKK KONTOL AJG BABI CUKIMAYYY MML PUKIIIIII!`")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    await rk.get_chat()
    a = b = 0
    if rk.is_private:
        user = rk.chat
        reason = rk.pattern_match.group(1)
    try:
        user, reason = await get_user_from_event(rk)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await rkp.edit("**GABISA BANG GATAU KENAPA.**")
    if user:
        if user.id == DEVS:
            return await rkp.edit("**LUTPAN MASA MAU DIKICK WKAKKWKAKAKWKWKWKAKSJSKAK**")
        try:
            await rk.client(BlockRequest(user))
            await rk.client(UnblockRequest(user))
        except BaseException:
            pass
        testrk = [
            d.entity.id
            for d in await rk.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testrk:
            try:
                await rk.client.edit_permissions(i, user, view_messages=False)
                await rk.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await rkp.edit(
                    f"`Waitttt kata Lutpan{a} `"
                )

            except BaseException:
                b += 1
    else:
        await rkp.edit("`KATA LUTPAN DIREPLY BIAR DONE`")

    return await rkp.edit(
        f"**DONE BUAT KICK INI MAKHLUK ** [{user.first_name}](tg://user?id={user.id}) **DI {a} TEMPAT ANGKER**"
    )


CMD_HELP.update(
    {
        "gkick": f"**Plugin : **`gkick`\
        \n\n  •  **Syntax :** `{cmd}gkick` <alasan>\
        \n  •  **Function : **kick pengguna secara global dari semua Administrasi Grup di mana Anda berada.\
    "
    }
)
