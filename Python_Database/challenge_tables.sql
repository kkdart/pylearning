-- Create employee table
CREATE TABLE authors(
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
)

CREATE TABLE books(
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    pages INT NOT NULL
)

CREATE TABLE author_books(
    id SERIAL PRIMARY KEY,
    author_id INT NOT NULL,
    book_id INT NOT NULL
)