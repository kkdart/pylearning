#win pip3 install psycopg2
#mac os pip3 install psycopg2-binary

import time
import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(database ="red30",
    user="postgres",
    password="pwtesting",
    host="10.1.1.40",
    port="5432")

cur = conn.cursor()

#Query to create transaction
create_transaction = '''CREATE TABLE IF NOT EXISTS transaction (
    id SERIAL PRIMARY KEY,
    cal_week TEXT NOT NULL,
    product VARCHAR(20) NOT NULL,
    cost INT);'''

cur.execute(create_transaction)

print("Created Table")

# #Insert data from a csv into the sales table
# with open('/Users/kyryl/Desktop/transactions.csv','r') as f:
#     # Notice that we don't need the `csv` module.
#     next(f) # Skip the header row.
#     cur.copy_from(f, 'transaction', sep=',', columns = ('cal_week', 'product', 'cost'))


#Query to create sales table
create_temp_transaction = '''CREATE TEMPORARY TABLE IF NOT EXISTS temp_transaction(
    cal_week TEXT NOT NULL,
    product VARCHAR(20) NOT NULL,
    cost INT);'''

cur.execute(create_temp_transaction)

#Insert data from a csv into the sales table
with open('/Users/kyryl/Desktop/transaction2.csv','r') as f:
    # Notice that we don't need the `csv` module.
    next(f) # Skip the header row.
    cur.copy_from(f, 'temp_transaction', sep=',', columns = ('cal_week', 'product', 'cost'))

cur.execute(
    sql.SQL("DELETE FROM temp_transaction t2 WHERE cal_week=ANY(select distinct(cal_week) from transaction t);")
)

# #Makes sure temp table exists
# cur.execute(
#     sql.SQL("SELECT * FROM {new};")
#         .format(
#             new = sql.Identifier('temp_transaction'))
#         )

# print(cur.fetchall())

cur.execute(
    sql.SQL("INSERT INTO transaction (cal_week,product, cost) SELECT * FROM temp_transaction;")
)


time.sleep(1)

conn.commit()
conn.close()