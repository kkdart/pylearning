import sqlite3

connection = sqlite3.connect('movies.db')

cursor = connection.cursor()

#cursor.execute('''CREATE TABLE IF NOT EXISTS Movies (Title TEXT, Director TEXT, Year INT)''')
#cursor.execute("INSERT INTO Movies VALUES ('Taxi Driver','Martin Scorsese',1976)")

#cursor.execute("SELECT * FROM Movies")

# famousFilms = [('Pulp Fiction','Quentin Tarantino',1994),
# ('Back to the Future','Steven Spielberg',1985),
# ('Moonrise Kingdom','Wes Anderson', 2012)]

# cursor.executemany('Insert INTO Movies VALUES (?,?,?)',famousFilms)

# records = cursor.execute("Select * FROM Movies")

# #print(cursor.fetchone())
# print(cursor.fetchall())

# for record in records:
#     print(record)

release_year = (1985,)
print(type(release_year))

cursor.execute("SELECT * FROM Movies WHERE year = ?",release_year)

connection.commit()
connection.close()