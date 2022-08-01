# - *- coding: utf- 8 - *-
from aiogram.types import ReplyKeyboardMarkup

# static
skip_send_image_default = ReplyKeyboardMarkup(resize_keyboard=True)
skip_send_image_default.row("📸 Пропустить")

cancel_send_image_default = ReplyKeyboardMarkup(resize_keyboard=True)
cancel_send_image_default.row("📸 Отменить")
