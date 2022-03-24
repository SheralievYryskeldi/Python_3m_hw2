from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from bot_instance import dp, bot
from keyboeard_buttons import keyboard

async def greeter(message: types.Message):
    await bot.send_message(message.chat.id, "Здравствуйте, давайте ответим на пару вопросов",
                           reply_markup=keyboard.keyboard_stat)

async def result(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Уже знал",
                                         callback_data="button_call_1")
    markup.add(button_call_1)
    button_call_2 = InlineKeyboardButton("Было слегка трудно",
                                         callback_data="button_call_2")
    markup.add(button_call_2)
    button_call_3 = InlineKeyboardButton("Не знал этого",
                                         callback_data="button_call_3")
    markup.add(button_call_3)
    await bot.send_message(message.chat.id, "Как вы справились?", reply_markup=markup)

async def question1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_4 = InlineKeyboardButton("Закончили?",
                                         callback_data="button_call_4")
    markup.add(button_call_4)
    answers = ['1980', '1964', '1989', '1914']
    question = 'Когда Гвидо ван Россум начал создание питона?'
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=2,
                        explanation="Он приступил к созданию питона в декабре 1989 года",
                        explanation_parse_mode=ParseMode.MARKDOWN_V2,
                        reply_markup=markup)

async def question2(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_4 = InlineKeyboardButton("Закончили?",
                                         callback_data="button_call_4")
    markup.add(button_call_4)
    answers = ['PUBG', 'Overwatch', 'Dota2', 'Warcraft']
    question = 'В какой игре разработчики использовали питон для создания некоторых скриптов, серверной части игры и её логики?'
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=0,
                        explanation="PUBG",
                        explanation_parse_mode=ParseMode.MARKDOWN_V2,
                        reply_markup=markup)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(greeter, commands=['start'])
    dp.register_message_handler(question1, commands=['start_quiz'])
    dp.register_message_handler(question2, commands=['start_quiz2'])
    dp.register_message_handler(result, commands=['finished'])