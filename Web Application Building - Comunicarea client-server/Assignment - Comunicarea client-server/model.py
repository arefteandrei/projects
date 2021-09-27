import sqlite3


conn = sqlite3.connect('students.db')
cursor = conn.cursor()

def database():
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS Students(
            student_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            student_card_number INT NOT NULL,
            note TINYINT NOT NULL 
        )'''
    )
    conn.commit()

def save_in_db(name, last_name, student_card_number, note):
    cursor.execute(
        f'INSERT INTO Students VALUES (null,?,?,?,?)', (name, last_name, student_card_number, note)
    )
    conn.commit()

def data(student_card_number, value=None):
    cursor.execute(
        f'SELECT name, last_name, student_card_number, note FROM Students WHERE student_card_number = {student_card_number}'
    )
    data = cursor.fetchall()
    if data:
        if value == 'name':
            return data[0][0]
        elif value == 'last_name':
            return data[0][1]
        elif value == 'student_card_number':
            return data[0][2]
        elif value == 'note':
            lst = []
            if len(data) > 1:
                for i in range(len(data)):
                    lst.append(data[i][3])
                return sum(lst)/len(data)
            else:
                return data[0][3]
        else:
            return False


   
print(data(12))