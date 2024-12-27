from aiogram import Router, F, types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from config import db

complaints_router = Router()

class Comments(StatesGroup):
    name = State()
    phone_num = State()
    complaint = State()

@complaints_router.callback_query(F.data == "complaint")
async def start_complaint(callback: types.callback_query, state: FSMContext):
    await callback.answer()
    await callback.message.answer("Ваше имя?")
    await state.set_state(Comments.name)

@complaints_router.message(Comments.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name = message.text)
    await message.answer("Ваш номер телефона?")
    await state.set_state(Comments.phone_num)

@complaints_router.message(Comments.phone_num)
async def process_phone_num(message: types.Message, state: FSMContext):
    await state.update_data(phone_num = message.text)
    await message.answer('Оставьте свою жалобу')
    await state.set_state(Comments.complaint)

@complaints_router.message(Comments.complaint)
async def process_complaint(message: types.Message, state: FSMContext):
    await state.update_data(complaint = message.text)
    data = await state.get_data()
    print(data)
    db.save_complaints(data)
    await state.clear()
    await message.answer('Спасибо за отзыв!')
