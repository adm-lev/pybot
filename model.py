from sqlalchemy import create_engine, MetaData, Table, Integer, String, and_, \
    Column, DateTime, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from config import ENGINE, DBASE_NAME
from sqlalchemy.orm import sessionmaker
from weeks import find_week
from datetime import datetime, timedelta
from sqlalchemy.exc import SQLAlchemyError


Base = declarative_base()
engine = create_engine(ENGINE, echo=True)
Session = sessionmaker(bind=engine)


class Schedule(Base):
    __tablename__ = 'schedule'
    id = Column(Integer, autoincrement=True, primary_key=True, unique=True)
    date = Column(String(20), nullable=False)
    week_day = Column(String(10), nullable=False)
    time = Column(String(20), nullable=False)
    name = Column(String(50), nullable=True)
    info = Column(String(1000), nullable=True)
    status = Column(String(20), default='Free')

    def __init__(self, today: list, time: str, name: str, info: str, status: str):
        self.date = today[0]
        self.week_day = today[1]
        self.time = time
        self.name = name
        self.info = info
        self.status = status

    def __repr__(self):
        notice: str = f'Дата: {self.date}, День: {self.week_day}, Время: {self.time}, Статус: {self.status},' \
                      f' Имя: {self.name}, Заметки: {self.info}'
        return notice


"""---------------------Методы работы с данными----------------------------"""


def create_db():
    Base.metadata.create_all(engine)


def fill_week(session: Session, next_week=False) -> None:

    day = (datetime.now() + timedelta(days=7)).date() if next_week else datetime.now().date()
    sample = bool(session.query(Schedule).filter(Schedule.date == day).first())
    if sample:
        print(sample)
        return None

    template = find_week(next_week)
    for date in template[0]:
        for time in template[1]:
            schedule = Schedule(date, time, name='', info='', status='Свободно')
            session.add(schedule)
    session.commit()
    session.close()


def get_week(session: Session, next_week=False):
    day = (datetime.now() + timedelta(days=2)).date()    #  datetime.now().date()   #  if next_week else
    sample = session.query(Schedule).filter(Schedule.date == str(day)).all()#.first()

    session.close()

    return sample


def get_day(session: Session, day: str) -> list[dict]:
    result: list = []
    temp_dict: dict = {}
    sample = session.query(Schedule).filter(Schedule.date == day).all()

    for item in sample:
        temp = str(item).split(sep=' ')
        for k in range(0, len(temp), 2):
            temp_dict[temp[k][:-1]] = temp[k + 1][:-1]
        result.append(temp_dict)
        temp_dict = {}

    session.close()

    return result


test_call = 'lesson_4_2022-08-04'


def set_appointment(session: Session, info, name) -> str:

    number_lesson = [
        '10:00-11:00',
        '11:30-12:30',
        '13:00-14:00',
        '14:30-15:30',
        '16:00-17:00',
        '17:30-18:30',
    ]
    date = info[9:]
    time = int(info[7])

    try:
        record = session.query(Schedule).filter(and_(Schedule.date == date, Schedule.time == number_lesson[time])).one()

        print(record)
        record.name = name
        record.status = 'Записано'

        session.add(record)
        session.commit()

        print(record)

    except SQLAlchemyError as e:
        print(f'Error! {e}')
        return 'Не удалось сохранить запись'

    session.close()
    return 'Запись успешно сохранена!'





# print('start!!!')


# set_appointment(Session(), test_call, 'Вася')





