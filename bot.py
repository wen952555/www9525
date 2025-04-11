import os
from telegram.ext import ApplicationBuilder, CommandHandler
from handlers import (
    help_handler,
    shell_handler,
    subscription_handler,
    qr_code_handler,
    translate_handler,
    currency_handler,
    rss_handler,
    permission_handler,
    file_handler,
    schedule_handler,
)

def main():
    # 从环境变量加载配置
    token = os.getenv("BOT_TOKEN")
    webhook_url = os.getenv("WEBHOOK_URL")

    if not token or not webhook_url:
        raise ValueError("Error: BOT_TOKEN and WEBHOOK_URL must be set in environment variables.")

    # 创建 Telegram 应用程序
    application = ApplicationBuilder().token(token).build()

    # 注册命令处理器
    application.add_handler(CommandHandler("help", help_handler.handle))
    application.add_handler(CommandHandler("shell", shell_handler.handle))
    application.add_handler(CommandHandler("schedule_shell", shell_handler.schedule))
    application.add_handler(CommandHandler("convert_subscription", subscription_handler.handle))
    application.add_handler(CommandHandler("generate_qr", qr_code_handler.handle))
    application.add_handler(CommandHandler("translate", translate_handler.handle))
    application.add_handler(CommandHandler("convert_currency", currency_handler.handle))
    application.add_handler(CommandHandler("rss", rss_handler.handle))
    application.add_handler(CommandHandler("set_permission", permission_handler.handle))
    application.add_handler(CommandHandler("file", file_handler.handle))
    application.add_handler(CommandHandler("schedule", schedule_handler.handle))

    # 启动 Webhook
    application.run_webhook(
        listen="0.0.0.0",
        port=int(os.getenv("PORT", 8443)),
        url_path=token,
        webhook_url=f"{webhook_url}/{token}",
    )

if __name__ == "__main__":
    main()