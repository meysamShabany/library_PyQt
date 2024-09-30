import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()
sql = """
    CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY ,
    title VARCHAR(250),
    author VARCHAR(200),
    isnb VARCHAR(80),
    category VARCHAR(200)
    );
"""
cursor.execute(sql)
connection.commit()
connection.close()

def add_book(title , author , isnb , category):
    try:
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO books VALUES (NULL , ? , ? , ? , ?)", (title, author, isnb, category))
        connection.commit()
        connection.close()
        return 'success'
    except:
        return 'error'

def search_for_title(title):
    try:
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM books WHERE title LIKE ?" , ("%{}%".format(title) ,))
        res = cursor.fetchall()
        connection.commit()
        connection.close()
        return res
    except Exception as err:
        return err

def search_for_category(category):
    try:
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM books WHERE category LIKE ?" , ("%{}%".format(category) ,))
        res = cursor.fetchall()
        connection.commit()
        connection.close()
        return res
    except Exception as err:
        return err