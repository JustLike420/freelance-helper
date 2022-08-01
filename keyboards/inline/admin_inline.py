# - *- coding: utf- 8 - *-
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# static
test_keyboard = InlineKeyboardMarkup()
test1 = InlineKeyboardButton(text="test1", callback_data="test1")
test2 = InlineKeyboardButton(text="test2", callback_data="test2")
test_keyboard.add(test1, test2)
