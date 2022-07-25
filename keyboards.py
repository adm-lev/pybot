from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
""" ----------------- Main menu ----------------------------"""
btn_week1 = KeyboardButton('Эта неделя')
btn_week2 = KeyboardButton('Следующая неделя')
main_menu = InlineKeyboardMarkup().add(btn_week2, btn_week1)


"""-----------------------Other nemu-------------------------"""

btn_info = KeyboardButton('Инфо')
btn_money = KeyboardButton('Курс валют')
other_menu = InlineKeyboardMarkup().add(btn_money, btn_info)




if __name__ == '__main__':
    pass
