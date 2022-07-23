#win pip3 install psycopg2
#mac os pip3 install psycopg2-binary

import psycopg2

conn = psycopg2.connect(database ="red30",
    user="postgres",
    password="pwtesting",
    host="10.1.1.40",
    port="5432")

cur = conn.cursor()

#Query to create sales table
create_sales_table = '''CREATE TABLE IF NOT EXISTS Sales 
    (ORDER_NUM INT PRIMARY KEY,
        ORDER_TYPE TEXT,
        CUST_NAME TEXT,
        PROD_NUMBER TEXT,
        PROD_NAME TEXT,
        QUANTITY INT,
        PRICE REAL,
        DISCOUNT REAL,
        ORDER_TOTAL REAL);'''

cur.execute(create_sales_table)

#Insert data from a csv into the sales table
with open('/Users/kyryl/Desktop/red30-postgres.csv','r') as f:
    # Notice that we don't need the `csv` module.
    next(f) # Skip the header row.
    cur.copy_from(f, 'sales', sep=',')

conn.commit()
conn.close()