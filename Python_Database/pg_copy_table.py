#win pip3 install psycopg2
#mac os pip3 install psycopg2-binary

import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(database ="red30",
    user="postgres",
    password="pwtesting",
    host="10.1.1.40",
    port="5432")

cur = conn.cursor()

og_table = input("What is the table to copy from? ")
new_table = input("What would you like to copy the sales table into? ")

#Copy table from previous inputs
cur.execute(
    sql.SQL("CREATE TABLE {new} AS TABLE {og};")
        .format(
            new = sql.Identifier(new_table),
            og = sql.Identifier(og_table))
        )

#return first 5 rows from query
cur.execute(
    sql.SQL("SELECT * FROM {new} LIMIT 5;")
        .format(
            new = sql.Identifier(new_table))
        )

print(cur.fetchall())

conn.commit()
conn.close()