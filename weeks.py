import calendar
from datetime import datetime, timedelta

curr_date = datetime.now()
y = curr_date.year
m = curr_date.month
d = curr_date.day


def find_week2(next_week=False):                     #  Функция возвращает словарь с днями и часами текущей недели
    date = datetime.now()

    if next_week:
        date = date + timedelta(days=7)             #  Может возвращать следующую нелелю относительно текущей даты

    weeks = calendar.monthcalendar(date.year, date.month)
    this_week = []
                                                    #  Является ли текущая неделя последней в месяце?
    for n, week in enumerate(weeks):
        if date.day in week:
            this_week = week[:5]
            break

    if this_week[0]:                                #  Добавляет в конец недели числа следующего месяца.
        i = 1
        for j in range(1, 5):
            if this_week[j] == 0:
                this_week[j] = i
                i += 1
    else:                                           #  Добавляет в начало недели числа предыдущего месяца
        if date.month > 1:
            last_month_week = calendar.monthcalendar(date.year, date.month - 1)[-1]
        else:
            last_month_week = calendar.monthcalendar(date.year - 1, 12)[-1]

        temp_week = []
        for i in last_month_week:
            if i != 0:
                temp_week.append(i)
        for i in this_week:
            if i != 0:
                temp_week.append(i)

        this_week = temp_week       #  [-5:]

    return this_week


def find_week(next_week=False):
    date = datetime.now()
    week_day = calendar.weekday(date.year, date.month, date.day)
    date = date - timedelta(days=week_day)
    if next_week:
        date = date + timedelta(days=7)
    this_week = []
    headers = [
        'Понедельник',
        'Вторник',
        'Среда',
        'Четверг',
        'Пятница',
        'Суббота',
        'Воскресенье',
    ]
    for i in range(5):
        next_day = date + timedelta(days=i)
        this_week.append(f'{headers[i]} - {next_day.day}.{next_day.month:02}.{next_day.year}')

    return this_week


def make_timetable(next_week=False):
    work_week = find_week(next_week)
    day_table = {
        '10:00-11:00': True,
        '11:30-12:30': True,
        '13:00-14:00': True,
        '14:30-15:30': True,
        '16:00-17:00': True,
        '17:30-18:30': True,
    }
    timetable = {}
    for day in work_week:
        timetable[day] = day_table

    return timetable

if __name__ == '__main__':


    table = (make_timetable())

    print(type(table))