from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from config import ENGINE, DBASE_NAME
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine(ENGINE, echo=True)
Session = sessionmaker(bind=engine)


class Schedule(Base):
    __tablename__ = 'schedule'
    id = Column(Integer, autoincrement=True, primary_key=True, unique=True)
    date = Column(String(20), nullable=False)
    time = Column(String(20), nullable=False)
    info = Column(String(1000), nullable=True)
    name = Column(String(50), nullable=True)
    status = Column(String(20), default='Free')

    def __repr__(self):
        notice: str = f'Дата: {self.date}, Время: {self.time}, Статус: {self.status},' \
                      f' Имя: {self.name}, Заметки: {self.info}'
        return notice


"""---------------------Методы работы с данными----------------------------"""


def create_db():
    Base.metadata.create_all(engine)


def fill_test(session: Session):

    pass




    # schedule = Schedule(date, time, info, name, status)
    # session.add(schedule)





    """
        for _ in range(50):
        full_name = faker.name().split(' ')
        age = faker.random.randint(16, 25)
        address = faker.address()
        group = faker.random.choice(group_list)

        student = Student(full_name, age, address, group.id)
        session.add(student)

    session.commit()
    session.close()
    :param session:
    :return:
    """







