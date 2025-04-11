from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import threading
import os
import asyncio

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

def run_telegram_bot():
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # 从环境变量获取 Token
    app_builder = ApplicationBuilder().token(TOKEN).build()
    app_builder.add_handler(CommandHandler("start", start))
    app_builder.add_handler(CommandHandler("help", help_command))

    # 创建并设置 asyncio 事件循环
    asyncio.set_event_loop(asyncio.new_event_loop())
    print("Telegram Bot is running...")
    app_builder.run_polling()

# 启动 Telegram Bot 和 Flask 服务
if __name__ == "__main__":
    # 在新线程中运行 Telegram Bot
    threading.Thread(target=run_telegram_bot).start()
    # 启动 Flask Web 服务（监听 Render 平台要求的端口）
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)