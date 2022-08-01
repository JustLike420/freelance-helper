from aiogram import types
from loader import dp


# user

@dp.message_handler(text="О боте")
async def about(message: types.Message):
    await message.answer("О боте")


@dp.message_handler(text="Ключевые слова")
async def keywords(message: types.Message):
    user_keywords = ''  # get_user keywords from database

    await message.answer(f"Поиск на фриланс бирже осуществляется по ключевым словам.\n"
                         f"Ваши ключевые слова: {user_keywords}")


@dp.message_handler(text="Поиск по ключевым словам")
async def keywords_search(message: types.Message):
    await message.answer("Поиск по ключевым словам")


@dp.message_handler(text="Избранные")
async def favorite(message: types.Message):
    await message.answer('Избранные')


@dp.message_handler(text="Автор")
async def author(message: types.Message):
    await message.answer('Автор')


# admin
@dp.message_handler(text="Статистика")
async def stats(message: types.Message):
    await message.answer('Статистика')


@dp.message_handler(text="Поиск профиля")
async def user_search(message: types.Message):
    await message.answer('Поиск профиля')


@dp.message_handler(text="Рассылка")
async def mailing(message: types.Message):
    await message.answer('Рассылка')
