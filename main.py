#!/usr/bin/env python

from telegram.ext import (Updater, MessageHandler, Filters, RegexHandler)
import logging
import oborona


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def ooo(bot, update):
    text = update.message.text
    ooo = ["ooo", "OOO", "ооо", "ООО", "Ooo", "Ооо"]
    resp = "МОЯ ОБОРОНА!\n"
    if text in ooo:
        resp += oborona.get_oborona()
        update.message.reply_text(resp)


def main():
    token = ""
    with open("/opt/bots/telegram/access.token", "r") as f:
        token = f.read().strip()
    logger.info("Starting bot")
    updater = Updater(token)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, ooo))
    logger.info("Bot started")
    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    main()

