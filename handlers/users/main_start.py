from aiogram import types
from data import config
from loader import dp
from utils.db.work_with_database import SqlAlchemy

db = SqlAlchemy()


@dp.message_handler(commands='start')
async def start(message: types.Message):
    db.create_user(message.from_user.id, message.from_user.username)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Кнопк1', 'Кнопка2', 'Кнопка3']

    if str(message.from_user.id) in config.admins:
        buttons.append('Кнопка4')
        buttons.append('Кнопка5')
    markup.add(*buttons)

    await message.answer(f"🤘 Салют, {message.chat.username}!\n", reply_markup=markup)
