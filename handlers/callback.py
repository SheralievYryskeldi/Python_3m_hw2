from aiogram import Dispatcher, types
from aiogram.types import ParseMode
from bot_instance import bot, dp

async def result(call: types.CallbackQuery):
    result = "Напишите /finished"
    await bot.send_message(call.message.chat.id, result)

async def answer1(call: types.CallbackQuery):
    answer1 = "Отлично"
    await bot.send_message(call.message.chat.id, answer1)

async def answer2(call: types.CallbackQuery):
    answer2 = "Надеюсь вы справились"
    await bot.send_message(call.message.chat.id, answer2)

async def answer3(call: types.CallbackQuery):
    answer3 = "В следующий раз ответишь правильно"
    await bot.send_message(call.message.chat.id, answer3)

def register_callback(dp: Dispatcher):
    dp.register_callback_query_handler(answer1, lambda func: func.data == "button_call_1")
    dp.register_callback_query_handler(answer2, lambda func: func.data == "button_call_2")
    dp.register_callback_query_handler(answer3, lambda func: func.data == "button_call_3")
    dp.register_callback_query_handler(result, lambda func: func.data == "button_call_4")
