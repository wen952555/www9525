import os
import schedule
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder
from bot.commands import setup_commands
from bot.handlers import setup_handlers
from tasks import schedule_jobs
from utils.logger import setup_logger

load_dotenv()

# Set up logging
logger = setup_logger()

# Load environment variables
API_TOKEN = os.getenv("BOTTOKEN")

# Create Telegram Bot Application
app = ApplicationBuilder().token(API_TOKEN).build()

# Register commands and handlers
setup_commands(app)
setup_handlers(app)

# Schedule background jobs
schedule_jobs()

if __name__ == "__main__":
    logger.info("Starting the bot...")
    app.run_polling()