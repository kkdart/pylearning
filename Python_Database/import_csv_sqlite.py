import sqlite3
import csv

#dataset url = https://www.kaggle.com/datasets/deewakarchakraborty/zomato-restaurant-dataset/versions/1?resource=download

con = sqlite3.Connection("restaurant.db")

cur = con.cursor()

source_csv = open('restaurants.csv')
rows = csv.reader(source_csv)

#Skip initial row
next(rows)
print(type(rows))

#Create table
cur.execute('''CREATE TABLE IF NOT EXISTS restaurants (links TEXT, names TEXT, ratings TEXT, cuisine TEXT, price_for_one TEXT)''')

#Insert values into table
cur.executemany("INSERT INTO restaurants VALUES (?,?,?,?,?)",rows)

#View data after import
cur.execute("Select count(*) from restaurants")
# print(cur.fetchall())
print(cur.fetchone()[0])

cur.execute("Select * from restaurants")
print(cur.fetchone()[0])

con.commit()
con.close()