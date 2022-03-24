from aiogram import executor
from bot_instance import dp
from handlers import tasks, callback

tasks.register_handlers(dp)
callback.register_callback(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
