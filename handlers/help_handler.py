from telegram import Update
from telegram.ext import ContextTypes

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = """
    Available Commands:
    /help - Show this help message
    /shell <command> - Execute a remote shell command
    /schedule_shell <seconds> <command> - Schedule a shell command
    /convert_subscription <url> - Convert node subscription formats
    /generate_qr <text> - Generate a QR code
    /translate <text> - Translate text to another language
    /convert_currency <amount> <from_currency> <to_currency> - Convert currency
    /rss <url> - Subscribe to an RSS feed
    /set_permission <user_id> <level> - Set user permissions
    /file <upload|download> <file_name> - Manage files
    /schedule <task> <time> - Schedule a task
    """
    await update.message.reply_text(help_text)