""" Xiaomi.eu command handler """
from telethon import events

from uranus_bot.telegram_bot import DATABASE
from uranus_bot.telegram_bot.messages.error import error_message
from uranus_bot.telegram_bot.messages.xiaomi_eu import eu_message
from uranus_bot.telegram_bot.tg_bot import BOT, PROVIDER


@BOT.on(events.NewMessage(pattern='/eu (.+)'))
async def xiaomi_eu(event):
    """Send a message when the command /eu is sent."""
    locale = DATABASE.get_locale(event.chat_id)
    device = event.pattern_match.group(1)
    if device not in list(PROVIDER.eu_codenames.keys()):
        await event.reply(await error_message(device, locale))
        return
    try:
        message, buttons = await eu_message(device, PROVIDER.eu_data, PROVIDER.eu_codenames, locale)
        await event.reply(message, buttons=buttons, link_preview=False)
    except TypeError:
        pass
    raise events.StopPropagation
