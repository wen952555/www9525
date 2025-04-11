import io
from telegram import Update
from telegram.ext import ContextTypes
from utils.qr_code_generator import generate_qr_code

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle the /generate_qr command to generate a QR code.
    """
    text = " ".join(context.args)
    if not text:
        await update.message.reply_text("Please provide text or a link to generate a QR code.")
        return

    try:
        qr_image = generate_qr_code(text)
        buffer = io.BytesIO()
        qr_image.save(buffer, format="PNG")
        buffer.seek(0)

        await update.message.reply_photo(photo=buffer, caption="Here is your QR code!")
    except Exception as e:
        await update.message.reply_text(f"Error generating QR code: {e}")