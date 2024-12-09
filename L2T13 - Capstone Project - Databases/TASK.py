import sqlite3

def connect_db():
    """Connect to the ebookstore database and return the connection and cursor."""
    conn = sqlite3.connect('ebookstore.db')
    cursor = conn.cursor()
    return conn, cursor


def create_table(cursor):
    """Create the book table if it doesn't exist and populate it with predefined books."""
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS book (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        qty INTEGER NOT NULL CHECK (qty >= 0)
    )
    ''')

    # Populate the table with initial data
    cursor.executescript('''
    INSERT OR IGNORE INTO book (title, author, qty) VALUES 
    ('A Tale of Two Cities', 'Charles Dickens', 30),
    ('Harry Potter and the Philosopher''s Stone', 'J.K. Rowling', 40),
    ('The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25),
    ('The Lord of the Rings', 'J.R.R. Tolkien', 37),
    ('Alice in Wonderland', 'Lewis Carroll', 12);
    ''')


def enter_book(cursor):
    """Add a new book to the database."""
    try:
        title = input('Enter the book title: ')
        author = input('Enter the author name: ')
        qty = int(input('Enter the quantity: '))
        
        cursor.execute('INSERT INTO book (title, author, qty) VALUES (?, ?, ?)', (title, author, qty))
        print('Book added successfully!')
    except ValueError:
        print('Invalid quantity entered. Please enter a valid number.')
    except sqlite3.IntegrityError:
        print('Error: Could not add book. Please check the input values.')


def update_book(cursor):
    """Update book information in the database."""
    try:
        id = int(input('Enter the book ID to update: '))
        column = input('Which field do you want to update? (title, author, qty): ')
        
        if column not in ['title', 'author', 'qty']:
            print('Invalid field. Please choose title, author, or qty.')
            return
        
        new_value = input('Enter the new value: ')
        if column == 'qty':
            new_value = int(new_value)
        
        cursor.execute(f'UPDATE book SET {column} = ? WHERE id = ?', (new_value, id))
        print('Book updated successfully!')
    except ValueError:
        print('Invalid input value. Please enter a valid number.')
    except sqlite3.IntegrityError:
        print('Error: Could not update book. Please check the input values.')


def delete_book(cursor):
    """Delete a book from the database."""
    try:
        id = int(input('Enter the book ID to delete: '))
        cursor.execute('DELETE FROM book WHERE id = ?', (id,))
        print('Book deleted successfully!')
    except ValueError:
        print('Invalid ID entered. Please enter a valid number.')
    except sqlite3.IntegrityError:
        print('Error: Could not delete book. Please check the input values.')


def search_books(cursor):
    """Search for a book by title or author."""
    search_term = input('Enter the book title or author to search for: ')
    cursor.execute('SELECT * FROM book WHERE title LIKE ? OR author LIKE ?', ('%' + search_term + '%', '%' + search_term + '%'))
    results = cursor.fetchall()
    
    if results:
        for row in results:
            print(f'ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Quantity: {row[3]}')
    else:
        print('No books found matching that search.')


def main():
    """Main menu loop for the ebookstore."""
    conn, cursor = connect_db()
    create_table(cursor)
    
    while True:
        print('\nMenu:')
        print('1. Enter book')
        print('2. Update book')
        print('3. Delete book')
        print('4. Search books')
        print('0. Exit')

        choice = input('Enter your choice (0-4): ')

        if choice == '1':
            enter_book(cursor)
        elif choice == '2':
            update_book(cursor)
        elif choice == '3':
            delete_book(cursor)
        elif choice == '4':
            search_books(cursor)
        elif choice == '0':
            conn.commit()  # Save changes before exiting
            conn.close()
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please select a valid option.')

        conn.commit()  # Save changes after each operation


if __name__ == "__main__":
    main()


