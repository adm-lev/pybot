import os
from models.database import DATABASE_NAME, Session
import models.create_database as db_creator
from models.lesson import Lessons, association_table
from models.students import Student
from models.group import Group
from sqlalchemy import and_


if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

    session = Session()
    for it in session.query(Lessons):
        print(it)
    print('*' * 30)
    for it in session.query(Lessons).filter(Lessons.id > 3):
        print(it)
    print('*' * 30)
    for it in session.query(Lessons).filter(and_(Lessons.id >= 3, Lessons.lessons_title.like('Ф%'))):
        print(it)
    print('*' * 30)
    for it in session.query(Student).join(Group).filter(Group.group_name == '1-MDA-7'):
        print(it)
    print('*' * 30)
    for it, gr in session.query(Student, Group):
        print(it, gr)
    print('*' * 30)
    for it in session.query(Lessons.lessons_title, Group.group_name).filter(and_(
            association_table.c.lesson_id == Lessons.id,
            association_table.c.group_id == Group.id,
            Group.group_name == '1-MDA-9'
    )):
        print(it)
    print('*' * 30)




