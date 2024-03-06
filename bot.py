import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers import answers_for_buttons, greeting


load_dotenv()

async def main():
    token = os.getenv('BOT_TOKEN')
    bot = Bot(token)
    dp = Dispatcher()

    dp.include_routers(greeting.router, answers_for_buttons.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

