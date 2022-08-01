# - *- coding: utf- 8 - *-
from aiogram.types import ReplyKeyboardMarkup

from data.config import admins


def main_menu(user_id):
    menu_default = ReplyKeyboardMarkup(resize_keyboard=True)
    menu_default.row("поле меню1", "поле меню2", "поле меню3")
    menu_default.row("поле меню4")
    if str(user_id) in admins:
        menu_default.row("поле меню админа 1", "поле меню админа 2")
        menu_default.row("поле меню админа 3", "поле меню админа 4", "поле меню админа 5")
    return menu_default


all_back_to_main_default = ReplyKeyboardMarkup(resize_keyboard=True)
all_back_to_main_default.row("⬅ На главную")
