import calendar
from datetime import datetime, timedelta
#
# curr_date = datetime.now()
# y = curr_date.year
# m = curr_date.month
# d = curr_date.day


def find_week(next_week=False) -> tuple:
    date = datetime.now()
    week_day = calendar.weekday(date.year, date.month, date.day)
    date = date - timedelta(days=week_day)
    if next_week:
        date = date + timedelta(days=7)

    dates: list = []
    headers: list = [
        'Понедельник',
        'Вторник',
        'Среда',
        'Четверг',
        'Пятница',
    ]
    day_table: list = [
        '10:00-11:00',
        '11:30-12:30',
        '13:00-14:00',
        '14:30-15:30',
        '16:00-17:00',
        '17:30-18:30',
    ]

    for i in range(5):
        next_day = date + timedelta(days=i)
        dates.append([f'{next_day.year}-{next_day.month:02}-{next_day.day:02}', headers[i]])

    res_week: tuple = (dates, day_table)

    return res_week


if __name__ == '__main__':

    pass
