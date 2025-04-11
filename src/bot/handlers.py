from telegram.ext import MessageHandler, Filters

def log_message(update, context):
    user_id = update.message.from_user.id
    message = update.message.text
    # Save chat log to database
    # Add your database logic here

def setup_handlers(app):
    app.add_handler(MessageHandler(Filters.text & ~Filters.command, log_message))