from aiogram import types
from filters import IsAdmin
from loader import dp


@dp.message_handler(IsAdmin(), text="admin")
async def admin(message: types.Message):
    await message.answer("admin_test")


@dp.message_handler(IsAdmin(), text="Статистика")
async def stats(message: types.Message):
    """
    Кол-во юзеров
    Кол-во избранных
    Кол-во за сегодня
    """
    await message.answer('Статистика')


@dp.message_handler(IsAdmin(), text="Поиск профиля")
async def user_search(message: types.Message):
    await message.answer('Поиск профиля')


@dp.message_handler(IsAdmin(), text="Рассылка")
async def mailing(message: types.Message):
    await message.answer('Рассылка')
