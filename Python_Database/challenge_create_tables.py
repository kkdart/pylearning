#win pip3 install psycopg2
#mac os pip3 install psycopg2-binary

import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(database ="challenge",
    user="postgres",
    password="pwtesting",
    host="10.1.1.40",
    port="5432")

cur = conn.cursor()

create_athors_table = '''CREATE TABLE IF NOT EXISTS authors(
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);'''

create_books_table = '''CREATE TABLE IF NOT EXISTS books(
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    pages INT NOT NULL
);'''

create_athor_books_table = '''CREATE TABLE IF NOT EXISTS author_books(
    id SERIAL PRIMARY KEY,
    author_id INT NOT NULL,
    book_id INT NOT NULL
);'''

cur.execute(create_athors_table)
cur.execute(create_books_table)
cur.execute(create_athors_table)

#Created Tables ^

conn.commit()
conn.close()