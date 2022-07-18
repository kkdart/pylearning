-- Create employee table
CREATE TABLE employee(
    ID SERIAL PRIMARY KEY,
    NAME TEXT NOT NULL,
    AGE INT NOT NULL,
    SALARY REAL
)