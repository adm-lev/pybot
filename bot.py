from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN, ENGINE
from sqlalchemy import create_engine
import calendar
from weeks import make_timetable
import keyboards as kb
from aiogram.dispatcher.filters import Text


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
engine = create_engine(ENGINE)
engine.connect()
cur_week = make_timetable()
next_week = make_timetable(True)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name}')


@dp.message_handler(commands='menu')
async def test_commands(message: types.Message):
    await list_categories(message)

async def list_categories(message: [types.Message, types.CallbackQuery], **kwargs):
    # markup = await categories_keyboard()
    pass


# @dp.callback_query_handler(Text(startswith='week'))
# async def www_call(callback: types.callback_query):
#     res = int(callback.data.split('_')[1])
#     await callback.answer('OK!')
#
#     await callback.answer()







if __name__ == '__main__':
    executor.start_polling(dp)
