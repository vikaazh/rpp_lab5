import sqlite3
from aiogram import Bot, Dispatcher, executor, types

conn = sqlite3.connect('users')
cursor = conn.cursor()
cursor.execute("""create table if not exists users( id integer primary key, name text, email text)""")
conn.commit()

def insert_value (id, name, email):
    conn = sqlite3.connect('users')
    cursor = conn.cursor()
    cursor.execute("""insert into users  (id, name, email) values (:id,:name,:email) """, {"id":id, "name":name, "email":email})
    conn.commit()
def select_func ():
    cursor = conn.cursor()
    cursor.execute("""select * from users""")
    print(cursor.fetchall())

def select_user(id):
    cursor = conn.cursor()
    cursor.execute("""select * from users where id=:id""",{"id":id})
    print(cursor.fetchall())
def select_user2(id,name):
    cursor = conn.cursor()
    cursor.execute("""select * from users where id=:id and name=:name """,{"id":id,"name":name})
    print(cursor.fetchall())


def delete_user(id):
    cursor = conn.cursor()
    cursor.execute("""delete from users where id=:id""",{"id":id})
    print(cursor.fetchall())
    conn.commit()


def main():
    # insert_value(1,'Дарья','555@mail.ru')
    # insert_value(2, 'Виктория', '888@mail.ru')
    # insert_value(3, 'Аврора', '111@mail.ru')
    # insert_value(4, 'Марк', '1968@mail.ru')
    # insert_value(5, 'Пётр', '1667@mail.ru')
    # insert_value(6, 'Екатерина', '1769@mail.ru')
    # insert_value(7, 'Елизавета', '1727@mail.ru')
    # insert_value(8,'Иван','1760@mail.ru')
    # insert_value(9,'Павел','1801@mail.ru')
    # insert_value(10,'Александр 1','1803@mail.ru')

    select_func()
    select_user(5)
    delete_user(13)
    select_user2(2, 'Виктория')
    select_func()

main()
conn.close()
















