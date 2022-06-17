import sqlite3

connection = sqlite3.connect('challenge.db')

cursor = connection.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS Users
# (User_Id INTEGER PRIMARY KEY AUTOINCREMENT, First_Name TEXT, Last_Name TEXT, Email TEXT)''')

# user_list = [("John", "Smith", "jsmith@gmail.com"),
# ("Johnny", "Appleseed", "jseed@gmail.com"),
# ("Steph", "Curry", "scurry@gmail.com"),
# ("Steven", "Smith", "ssmith@gmail.com"),
# ("Bob", "Oregon", "boregon@gmail.com")]


# cursor.executemany('INSERT INTO Users (first_name, last_name, email) VALUES (?,?,?)',user_list)

# connection.commit()


# records = cursor.execute("SELECT * from Users")
# print(cursor.fetchall())

records = cursor.execute("SELECT Email from Users")
print(cursor.fetchall())

connection.close()