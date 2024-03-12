import sqlite3
import random

class BookDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Book (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                pages INTEGER,
                cover_type TEXT,
                category TEXT
            )
        """)
        self.conn.commit()

    def generate_random_book(self):
        name = random.choice(["Pride and Prejudice", "Anna Karenina", "Crime and Punishment", "Don Quixote", "Lord of the Rings", "Hamlet",
                              "War and Peace", "To Kill a Mockingbird", "The Great Gatsby", "1984", "Brave New World", "The Catcher in the Rye",
                              "Moby-Dick", "The Odyssey", "The Iliad", "Frankenstein", "Dracula", "The Count of Monte Cristo", "The Picture of Dorian Gray",
                              "The Hobbit", "Alice's Adventures in Wonderland", "The Shining", "The Grapes of Wrath", "One Hundred Years of Solitude",
                              "The Brothers Karamazov", "Les Misérables", "The Hitchhiker's Guide to the Galaxy", "A Tale of Two Cities", "The Scarlet Letter",
                              "The Old Man and the Sea", "Gone with the Wind", "Wuthering Heights", "The Jungle", "The Sound and the Fury", "Atlas Shrugged"])
        pages = random.randint(50, 500)
        cover_type = random.choice(["Hardcover", "Paperback", " Softcover", "E-book"])
        category = random.choice(["Fiction", "Non-Fiction", "Science Fiction", "Mystery", "Fantasy", "Horror", "Romance", "Adventure", "Historical fiction", "Thriller", "Magical realism"])
        return name, pages, cover_type, category

    def insert_random_books(self, num_books):
        for _ in range(num_books):
            book_data = self.generate_random_book()
            self.cursor.execute("""
                INSERT INTO Book (name, pages, cover_type, category)
                VALUES (?, ?, ?, ?)
            """, book_data)
        self.conn.commit()

    def get_average_pages(self):
        self.cursor.execute("SELECT AVG(pages) FROM Book")
        return self.cursor.fetchone()[0]

    def get_largest_book_name(self):
        self.cursor.execute("SELECT name FROM Book ORDER BY pages DESC LIMIT 1")
        return self.cursor.fetchone()[0]

    def close_connection(self):
        self.conn.close()

book_db = BookDatabase("books.db")
book_db.create_table()
book_db.insert_random_books(10)

average_pages = book_db.get_average_pages()
print(f"Average Number of Pages: {average_pages}")

largest_book_name = book_db.get_largest_book_name()
print(f"The Largest Book is: {largest_book_name}")

book_db.close_connection()
