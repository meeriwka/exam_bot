from aiogram import Router, types
from aiogram.filters import Command

start_router = Router()

@start_router.message(Command('start'))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Нажмите, чтобы оставить жалобу", callback_data="complaint")
            ]

        ]

    )
    await message.answer(f'Привет, {name}!', reply_markup=kb)