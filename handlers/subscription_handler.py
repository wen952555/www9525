from telegram import Update
from telegram.ext import ContextTypes
from utils.subscription_converter import convert_subscription

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    link = " ".join(context.args)
    if not link.startswith("http"):
        await update.message.reply_text("Please provide a valid subscription link.")
        return

    try:
        converted_link = convert_subscription(link)
        await update.message.reply_text(f"Converted Subscription Link:\n{converted_link}")
    except Exception as e:
        await update.message.reply_text(f"Error converting subscription: {e}")