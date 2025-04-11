from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import threading
import os

# Flask Web Server
app = Flask(__name__)

@app.route("/")
def home():
    return "Telegram Bot is running!"

# Telegram Bot Handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Hello, {update.effective_user.first_name}!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("This is a simple Telegram bot. Use /start to begin!")

def run_flask():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    # 从环境变量中获取 Telegram Bot Token
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

    # 创建 Telegram Bot 应用
    app_builder = ApplicationBuilder().token(TOKEN).build()
    app_builder.add_handler(CommandHandler("start", start))
    app_builder.add_handler(CommandHandler("help", help_command))

    # 在新线程中运行 Flask 服务
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # 在主线程中运行 Telegram Bot
    print("Telegram Bot is running...")
    app_builder.run_polling()