import aiogram.types.inline_keyboard
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from weeks import find_week
from model import Session, get_day
from datetime import datetime


""" ----------------- Main menu ----------------------------"""
btn_week1 = InlineKeyboardButton('Эта неделя', callback_data='week1')
btn_week2 = InlineKeyboardButton('Следующая неделя', callback_data='week2')
main_menu = InlineKeyboardMarkup().add(btn_week1, btn_week2)


"""-----------------sum Main menu---------------------------------"""

btn_sub_week = InlineKeyboardButton('Хочу записаться на прием', callback_data='show_free')
btn_sub_show = InlineKeyboardButton('Хочу посмотреть журнал', callback_data='show_all')
sub_main_menu = InlineKeyboardMarkup().add(btn_sub_week, btn_sub_show)


"""-----------------------Other nemu-------------------------"""

btn_money = InlineKeyboardButton('Донат1', callback_data='clb_1')
btn_info = InlineKeyboardButton('Информация2', callback_data='clb_2')
other_menu = InlineKeyboardMarkup().add(btn_money, btn_info)

"""-------------------------Third layer--------------------------"""

# btn_monday1 = InlineKeyboardButton('Неделя1 День1', callback_data='day_1')
# btn_tuesday1 = InlineKeyboardButton('Неделя1 День2', callback_data='day_2')
# week1_menu = InlineKeyboardMarkup().add(btn_monday1, btn_tuesday1)
#
# btn_monday2 = InlineKeyboardButton('Неделя2 День1', callback_data='day_1')
# btn_tuesday2 = InlineKeyboardButton('Неделя2 День2', callback_data='day_2')
# week2_menu = InlineKeyboardMarkup().add(btn_monday2, btn_tuesday2)

"""----------------------------week keyboard--------------------------"""


def make_week_kb(next_week=False) -> InlineKeyboardMarkup:
    this_week = find_week(next_week)[0]
    dates = [n[0][5:] for n in this_week]
    btn_monday = InlineKeyboardButton(f'Пн-{dates[0]}', callback_data='day_1')
    btn_tuesday = InlineKeyboardButton(f'Вт-{dates[1]}', callback_data='day_2')
    btn_wednesday = InlineKeyboardButton(f'Ср-{dates[2]}', callback_data='day_3')
    btn_thursday = InlineKeyboardButton(f'Чт-{dates[3]}', callback_data='day_4')
    btn_friday = InlineKeyboardButton(f'Пт-{dates[4]}', callback_data='day_5')
    btn_back = InlineKeyboardButton('Назад', callback_data='day_0')
    return InlineKeyboardMarkup().add(
                                            btn_monday,
                                            btn_tuesday,
                                            btn_wednesday,
                                            btn_thursday,
                                            btn_friday,
                                            btn_back
                                        )


"""--------------------------------make day--------------------------"""


def make_day(date: str) -> InlineKeyboardMarkup:
    date: str = str(datetime.now().year) + date[2:]
    day_table: list = [
        '10:00-11:00',
        '11:30-12:30',
        '13:00-14:00',
        '14:30-15:30',
        '16:00-17:00',
        '17:30-18:30',
    ]

    day_info: list[dict] = get_day(Session(), date)

    day_kb = InlineKeyboardMarkup()

    btn_less_1 = InlineKeyboardButton
    btn_less_2 = InlineKeyboardButton
    btn_less_3 = InlineKeyboardButton
    btn_less_4 = InlineKeyboardButton
    btn_less_5 = InlineKeyboardButton
    btn_less_6 = InlineKeyboardButton

    btn_list: list = [btn_less_1, btn_less_2, btn_less_3, btn_less_4, btn_less_5, btn_less_6]
    for number, lesson in enumerate(btn_list):
        if day_info[number]['Статус'] == 'Свободно':
            lesson = InlineKeyboardButton(f'{day_table[number]}', callback_data=f'lesson_{number}_{date}')
            day_kb.add(lesson)

    return day_kb


def show_free_time():
    pass




if __name__ == '__main__':
    pass

    # print(type(week2_menu))
