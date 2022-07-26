from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN, ENGINE, DBASE_NAME

import os
from weeks import make_timetable
import keyboards as kb
from aiogram.dispatcher.filters import Text
import logging
from model import Schedule, create_db


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
db_is_created = os.path.exists(DBASE_NAME)
if not db_is_created:
    create_db()

cur_week = make_timetable()
next_week = make_timetable(True)


# engine.connect()


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name}')


@dp.message_handler(commands='menu')
async def test_commands(message: types.Message):
    await message.reply('Главное меню', reply_markup=kb.main_menu)


@dp.callback_query_handler(Text(startswith='week'))
async def main_nemu(call: types.CallbackQuery):
    if call.data == 'week1':
        await call.message.reply('первая неделя', reply_markup=kb.other_menu)

    else:
        await call.message.reply('вторая неделя', reply_markup=kb.other_menu)


@dp.callback_query_handler(Text(startswith='clb'))
async def main_nemu(call: types.CallbackQuery):
    if call.data == 'clb_1':
        await call.message.reply('расписание1', reply_markup=kb.week1_menu)

    else:
        await call.message.reply('расписание2', reply_markup=kb.week2_menu)


if __name__ == '__main__':
    executor.start_polling(dp)
