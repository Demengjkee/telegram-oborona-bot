#!/usr/bin/env python

from telegram.ext import (Updater, MessageHandler, Filters, RegexHandler, InlineQueryHandler, Handler, CommandHandler)
import logging
import oborona

from telegram import InlineQueryResultArticle, InputTextMessageContent
from uuid import uuid4

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
OOO = ["ooo", "OOO", "ооо", "ООО", "Ooo", "Ооо"]


def gen_oborona_resp():
    resp = "МОЯ ОБОРОНА!\n"
    resp += oborona.get_oborona()
    return resp


def ooo(bot, update):
    logger.info(update.message)
    text = update.message.text
    if text in OOO:
        update.message.reply_text(gen_oborona_resp())


def tmp_ooo(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id, "ООО, " + gen_oborona_resp())
    logger.info("Has sent a message to a channel %s", chat_id)

def ooo_inline(bot, update):
    logger.info("111111")
    text = update.inline_query.query 
    logger.info(update.inline_query)
    update.inline_query.answer([InlineQueryResultArticle(
                id=uuid4(),
                title="OBORONA",
                input_message_content=InputTextMessageContent(gen_oborona_resp()))])

def main():
    token = ""
    with open("/opt/bots/telegram/access.token", "r") as f:
        token = f.read().strip()
    logger.info("Starting bot")
    updater = Updater(token)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, ooo))
    dp.add_handler(InlineQueryHandler(ooo_inline))
    dp.add_handler(CommandHandler("oborona", tmp_ooo))
    logger.info("Bot started")
    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    main()

