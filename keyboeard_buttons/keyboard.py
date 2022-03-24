from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_send_task = KeyboardButton("/start_quiz")
button_send_task2 = KeyboardButton("/start_quiz2")

keyboard_stat = ReplyKeyboardMarkup(resize_keyboard=True)

keyboard_stat.row(button_send_task, button_send_task2)