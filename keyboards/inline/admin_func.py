# - *- coding: utf- 8 - *-
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# dynamic
def some_admin_func(some):
    some_keyboard= InlineKeyboardMarkup()
    test1 = InlineKeyboardButton(text="test1", callback_data=f"show_purchases:{some}")
    test2 = InlineKeyboardButton(text="test2", callback_data=f"add_balance:{some}")
    some_keyboard.add(test1, test2)
    return some_keyboard
