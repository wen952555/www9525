from telegram import ReplyKeyboardMarkup

def main_keyboard():
    keyboard = [
        ["/translate", "/addtask"],
        ["/showtasks", "/remind"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)