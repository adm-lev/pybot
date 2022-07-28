from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN, ENGINE, DBASE_NAME
from model import engine

import os
import keyboards as kb
from aiogram.dispatcher.filters import Text
import logging
from model import create_db, fill_week, Session, get_week, set_appointment


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
db_is_created = os.path.exists(DBASE_NAME)
if not db_is_created:
    create_db()
engine.connect()


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name}')


@dp.message_handler(commands='menu')
async def test_commands(message: types.Message):
    await message.answer('Меню:', reply_markup=kb.sub_main_menu)


@dp.callback_query_handler(Text(startswith='week'))
async def main_nemu(call: types.CallbackQuery):
    if call.data == 'week1':
        await call.message.answer('Выберите день:', reply_markup=kb.make_week_kb())
    else:
        await call.message.answer('Выберите день:', reply_markup=kb.make_week_kb(True))


@dp.callback_query_handler(Text(startswith='show'))
async def main_nemu(call: types.CallbackQuery):
    #  Проверка существования записи в БД
    fill_week(Session())
    fill_week(Session(), True)
    await call.message.answer('Выберите неделю:', reply_markup=kb.main_menu)


@dp.callback_query_handler(Text(startswith='lesson'))
async def main_nemu(call: types.CallbackQuery):
    data = call.data
    # print(call.data)
    # print(call.from_user.username)
    code = set_appointment(Session(), data, call.from_user.username)

    await call.message.reply(code)


@dp.callback_query_handler(Text(startswith='day'))
async def main_nemu(call: types.CallbackQuery):
    if '0' in call.data:
        #  Код получает название кнопки, вернувшей данный колбек
        data = call.data
        for j in call.message.reply_markup.inline_keyboard:
            for i in j:
                if i['callback_data'] == data:
                    print(i['text'])
        # await call.message.reply('Выберите удобное время:', reply_markup=kb.make_week_kb())
    else:
        data = call.data
        for j in call.message.reply_markup.inline_keyboard:
            for i in j:
                if i['callback_data'] == data:
                    await call.message.reply('Выберите время:', reply_markup=kb.make_day(i['text']))





if __name__ == '__main__':
    executor.start_polling(dp)
