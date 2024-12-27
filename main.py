import asyncio

from handlers.complaints import complaints_router
from handlers.start import start_router
from config import bot, dp, db



async def main():
    db.create_tables()
    dp.include_router(start_router)
    dp.include_router(complaints_router)


    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())