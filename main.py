import asyncio

from aiogram.utils import executor
import filters
import middlewares
from handlers import dp
from utils import on_startup_notify
from utils.set_bot_commands import set_default_commands
from utils.db.work_with_database import SqlAlchemy

db = SqlAlchemy()


async def on_startup(dp):
    filters.setup(dp)
    middlewares.setup(dp)
    await set_default_commands(dp)
    # await on_startup_notify(dp)
    print("~~~~~ Bot was started ~~~~~")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
