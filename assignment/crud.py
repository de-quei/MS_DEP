import sqlite3

def create_table():
    connection = sqlite3.connect("students_info.db")
    cursor = connection.cursor()

    #만약 테이블이 존재한다면, 이 문장은 수행하지 않는다.
    cursor.execute('''CREATE TABLE IF NOT EXISTS students_info
                        (id INTEGER PRIMARY KEY, name TEXT,
                        age INTEGER, major TEXT)''')
    
    connection.commit()
    connection.close()

create_table()

def insert_student(name, age, major):
    connection = sqlite3.connect("students_info.db")
    cursor = connection.cursor()

    cursor.execute('''INSERT INTO students_info (name, age, major)
                                VALUES (?, ?, ?)''', (name, age, major))
            
    connection.commit()
    connection.close()

insert_student("Kim", 20, "Robotics")
insert_student("Yang", 22, "Data Science")
insert_student("Park", 23, "Artificial intelligence")
insert_student("Lee", 25, "Computer Enginnering")

def query_students():
    connection = sqlite3.connect("students_info.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students_info")
    rows = cursor.fetchall()
            
    connection.close()

    return rows

def delete_student(student_id):
    connection = sqlite3.connect("students_info.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM students_info WHERE id = ?", (student_id,))
            
    connection.commit()
    connection.close()

delete_student(2)
delete_student(3)
print(query_students())