from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
""" ----------------- Main menu ----------------------------"""
btn_week1 = InlineKeyboardButton('Эта неделя', callback_data='week1')
btn_week2 = InlineKeyboardButton('Следующая неделя', callback_data='week2')
main_menu = InlineKeyboardMarkup().add(btn_week2, btn_week1)


"""-----------------------Other nemu-------------------------"""

btn_money = InlineKeyboardButton('Донат1', callback_data='clb_1')
btn_info = InlineKeyboardButton('Информация2', callback_data='clb_2')
other_menu = InlineKeyboardMarkup().add(btn_money, btn_info)

"""-------------------------Third layer--------------------------"""

btn_monday1 = InlineKeyboardButton('Неделя1 День1', callback_data='day_1')
btn_tuesday1 = InlineKeyboardButton('Неделя1 День2', callback_data='day_2')
week1_menu = InlineKeyboardMarkup().add(btn_monday1, btn_tuesday1)

btn_monday2 = InlineKeyboardButton('Неделя2 День1', callback_data='day_1')
btn_tuesday2 = InlineKeyboardButton('Неделя2 День2', callback_data='day_2')
week2_menu = InlineKeyboardMarkup().add(btn_monday2, btn_tuesday2)




if __name__ == '__main__':
    pass
