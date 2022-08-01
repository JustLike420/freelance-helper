from aiogram import types
from keyboards import main_menu
from loader import dp
from utils.db.work_with_database import SqlAlchemy

db = SqlAlchemy()


@dp.message_handler(commands='start')
async def start(message: types.Message):
    db.create_user(message.from_user.id, message.from_user.username)
    markup = main_menu(message.from_user.id)
    await message.answer(f"🤘 Салют, {message.chat.username}!\n", reply_markup=markup)
