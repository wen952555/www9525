from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 定义 /start 命令的处理函数
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Hello, {update.effective_user.first_name}!")

# 定义 /help 命令的处理函数
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("This is a simple Telegram bot. Use /start to begin!")

if __name__ == "__main__":
    # 从环境变量中读取 Telegram Bot Token
    import os
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

    # 初始化应用程序
    app = ApplicationBuilder().token(TOKEN).build()

    # 添加命令处理器
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    # 启动应用程序
    print("Bot is running...")
    app.run_polling()