import sqlite3

conn = sqlite3.connect("my_db")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Books(
        id INT PRIMARY KEY,
        title TEXT,
        year INT);
        """)
conn.commit()

start_or_end = None

while start_or_end != '0':
    print(" "
          "\nYou have 3 options:"
          "\n   Please select 1 to insert data into the database."
          "\n   Please select 2 to view the data in the database."
          "\n   Please select 0 to end the program.")

    start_or_end = str(input("Enter your option here: "))

    if start_or_end == '1':
        primary_key = input("Please insert a primary key: ")
        title = input("Please insert title of Book: ")
        year = input("Please insert year of Book: ")

        books = (str(primary_key), str(title), int(year))
        cursor.execute("INSERT INTO Books VALUES (?, ?, ?)", books)
        conn.commit()

    elif start_or_end == '2':
        cursor.execute("SELECT * FROM Books;")
        all_results = cursor.fetchall()
        print(all_results)

    elif start_or_end == '0':
        break

    elif start_or_end != '0' or start_or_end != '1' or start_or_end != '2':
        print("The selected option is not valid. Please select a valid option.")

cursor.close()

conn.close()
