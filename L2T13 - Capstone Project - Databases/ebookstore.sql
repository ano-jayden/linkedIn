CREATE DATABASE ebookstore;

CREATE TABLE book (
    id INT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    qty INT
);

INSERT INTO book (id, title, author, qty) VALUES
(3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
(3002, 'Harry Potter and the Philosopher''s Stone', 'J.K. Rowling', 40),
(3003, 'The Lion, the Witch and the Wardrobe', 'C. S. Lewis', 25),
(3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37),
(3005, 'Alice in Wonderland', 'Lewis Carroll', 12);
