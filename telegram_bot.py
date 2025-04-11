import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 设置管理员的 Telegram 用户 ID（仅管理员可以执行某些命令）
ADMIN_ID = 123456789  # 替换为您自己的 Telegram 用户 ID

# 检查用户是否是管理员
def is_admin(update: Update) -> bool:
    return update.effective_user.id == ADMIN_ID

# /start 命令
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Hello, {update.effective_user.first_name}! I am your VPN manager bot.")

# /status 命令：检查服务器状态
async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update):
        await update.message.reply_text("You do not have permission to run this command.")
        return

    # 示例状态信息（可替换为实际的服务器状态查询逻辑）
    status_info = """
    VPN Server Status:
    - Active Users: 120
    - Online Users: 45
    - Server Load: 30%
    """
    await update.message.reply_text(status_info)

# /notify 命令：发送通知
async def notify(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update):
        await update.message.reply_text("You do not have permission to run this command.")
        return

    # 获取要发送的通知消息
    message = " ".join(context.args)
    if not message:
        await update.message.reply_text("Usage: /notify <message>")
        return

    # 示例：发送通知给所有用户（此处简单回复消息）
    await update.message.reply_text(f"Notification sent: {message}")

# /help 命令：显示帮助信息
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
    Available Commands:
    /start - Start the bot
    /status - Check VPN server status (admin only)
    /notify <message> - Send a notification to all users (admin only)
    """
    await update.message.reply_text(help_text)

# 主函数
def main():
    # 从环境变量加载 Telegram Bot Token
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    if not TOKEN:
        print("Error: TELEGRAM_BOT_TOKEN environment variable not set.")
        return

    # 创建应用程序
    app = ApplicationBuilder().token(TOKEN).build()

    # 添加命令处理程序
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("notify", notify))
    app.add_handler(CommandHandler("help", help_command))

    # 启动机器人
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()