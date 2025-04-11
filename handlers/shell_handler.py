from telegram import Update
from telegram.ext import ContextTypes
from utils.shell_executor import execute_shell_command, schedule_shell_command

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    command = " ".join(context.args)
    if not command:
        await update.message.reply_text("Please provide a command to execute.")
        return

    output = execute_shell_command(command, update.effective_user.id)
    await update.message.reply_text(output)

async def schedule(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if len(args) < 2:
        await update.message.reply_text("Usage: /schedule_shell <time_in_seconds> <command>")
        return

    time_in_seconds = int(args[0])
    command = " ".join(args[1:])
    schedule_shell_command(command, time_in_seconds, update.effective_user.id)
    await update.message.reply_text(f"Scheduled command '{command}' to run in {time_in_seconds} seconds.")