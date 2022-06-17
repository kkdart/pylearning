import sqlite3

connection = sqlite3.connect('challenge.db')

cursor = connection.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS Users(User_Id TEXT, First_Name TEXT, Last_Name TEXT, Email TEXT)''')

# user_list = [('1', "John", "Smith", "jsmith@gmail.com"),
# ('2', "Johnny", "Appleseed", "jseed@gmail.com"),
# ('3', "Steph", "Curry", "scurry@gmail.com"),
# ('4', "Steven", "Smith", "ssmith@gmail.com"),
# ('5', "Bob", "Oregon", "boregon@gmail.com")]


# cursor.executemany('INSERT INTO Users VALUES(?,?,?,?)',user_list)
# connection.commit()


# records = cursor.execute("SELECT * from Users")

# for i in records:
#     print(i)

records = cursor.execute("SELECT Email from Users")

for i in records:
    print(i)

connection.close()