import sqlite3

if __name__ == "__main__":
    connectTable = sqlite3.connect('school.db')
    cursor = connectTable.cursor()

    with open('script.sql') as file:
        cursor.executescript(file.read())

    connectTable.commit()

    connectTable.close()