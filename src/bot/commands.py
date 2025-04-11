from telegram.ext import CommandHandler
from bot.keyboards import main_keyboard
from functions.translate_utils import translate_text
from models import conn

def start(update, context):
    update.message.reply_text(
        "Welcome to the Advanced Telegram Bot!",
        reply_markup=main_keyboard()
    )

def translate(update, context):
    text = " ".join(context.args)
    if not text:
        update.message.reply_text("Usage: /translate {text}")
        return

    translated_text = translate_text(text)
    update.message.reply_text(translated_text)

def setup_commands(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("translate", translate))