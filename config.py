from dotenv import dotenv_values
from aiogram import Bot, Dispatcher
from database import Database



token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()
db = Database('data.sqlite3')

