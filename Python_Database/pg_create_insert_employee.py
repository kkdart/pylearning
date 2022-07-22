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
create_employee = '''CREATE TABLE IF NOT EXISTS employee(
    ID SERIAL PRIMARY KEY,
    NAME TEXT NOT NULL,
    AGE INT NOT NULL,
    SALARY DECIMAL);'''

cur.execute(create_employee)

#Insert data from a csv into the sales table
with open('/Users/kyryl/Desktop/load.csv','r') as f:
    # Notice that we don't need the `csv` module.
    next(f) # Skip the header row.
    cur.copy_from(f, 'employee', sep=',', columns = ('name', 'age', 'salary'))

conn.commit()
conn.close()