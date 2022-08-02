from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards import keywords_button, all_back_to_main_default, main_menu, sure_edit_keywords
from loader import dp
from utils.db.work_with_database import SqlAlchemy

db = SqlAlchemy()


@dp.message_handler(text="О боте")
async def about(message: types.Message):
    await message.answer("Это бот служит для отслеживания и отправки новых проектов "
                         "с различшных фриланс бирж по ключевым словам.")


@dp.message_handler(text="Ключевые слова")
async def keywords(message: types.Message):
    user_keywords = db.get_keywords(message.from_user.id)
    await message.answer(f"Поиск на фриланс бирже осуществляется по ключевым словам.\n"
                         f"Ваши ключевые слова: {user_keywords}", reply_markup=keywords_button)


@dp.callback_query_handler(text='change_keywords')
async def add_keywords(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("Введите новые ключевые слова через запятую:", reply_markup=all_back_to_main_default)
    # await KeywordsState.keywords_string.set()
    await state.set_state("get_keywords")


@dp.message_handler(state="get_keywords")
async def add_keywords_db(message: types.Message, state: FSMContext):
    keywords_input = message.text
    await state.update_data(get_keywords=keywords_input)
    await state.set_state("edit_keywords_confirm")
    await message.answer("Вы хотите изменить ключевые слова на:\n"
                         f"{keywords_input}?", reply_markup=sure_edit_keywords)


@dp.callback_query_handler(text=['yes_edit_k', 'no_edit_k'], state='edit_keywords_confirm')
async def confirm_keywords(call: types.CallbackQuery, state: FSMContext):
    get_action = call.data.split("_")[0]
    keywords_text = (await state.get_data())['get_keywords']
    await state.finish()
    if get_action == "yes":
        db.change_keywords(call.from_user.id, keywords_text)
        await call.message.edit_text("Вы успешно изменили ключевые слова на:"
                                     f"{keywords_text}")
    else:
        await call.message.edit_text("Отменено")


@dp.callback_query_handler(text='clear_keywords')
async def clear_keywoards(call: types.CallbackQuery):
    db.change_keywords(call.from_user.id, '')
    await call.message.answer("Ключевые слова были очищены")


@dp.message_handler(text="Поиск по ключевым словам")
async def keywords_search(message: types.Message):
    await message.answer("Поиск по ключевым словам")


@dp.message_handler(text="Избранные")
async def favorite(message: types.Message):
    await message.answer('Избранные')


@dp.message_handler(text="Автор")
async def author(message: types.Message):
    await message.answer("Автор бота: <a href='https://t.me/Squishy666'>Vladimir</a>", parse_mode=types.ParseMode.HTML,
                         disable_web_page_preview=True)


