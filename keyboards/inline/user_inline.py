# - *- coding: utf- 8 - *-
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# static
keywords_button = InlineKeyboardMarkup()
change = InlineKeyboardButton(text="Изменить", callback_data="change_keywords")
clear = InlineKeyboardButton(text="Очистить", callback_data="clear_keywords")
keywords_button.add(change, clear)

sure_edit_keywords = InlineKeyboardMarkup()
yes_edit_k = InlineKeyboardButton(text="✅ Изменить", callback_data="yes_edit_k")
no_edit_k = InlineKeyboardButton(text="❌ Отменить", callback_data="no_edit_k")
sure_edit_keywords.add(yes_edit_k, no_edit_k)