## Overview
This Python script demonstrates the use of SQLite to create a simple book database, generate random book entries, and perform basic queries on the database. The `BookDatabase` class provides methods to create a table, insert random books, calculate the average number of pages, and find the largest book based on the number of pages.

## Installation

1. Clone or download the project repository.
2. Install the required dependencies using the provided requirements.txt file:

```py
pip install -r requirements.txt
```
3. After installing the dependencies, run the run.py file to start the Figure calculator app.
```py
python main.py
```

## Usage
The BookDatabase class has several methods:

- **create_table()**:
This method creates a table named "Book" in the SQLite database if it doesn't already exist. The table has columns for book ID, name, number of pages, cover type, and category.

- **generate_random_book()**:
This method generates random book data, including a name, number of pages, cover type, and category.

- **insert_random_books(num_books)**:
This method inserts a specified number of randomly generated books into the database.

- **get_average_pages()**:
This method calculates and returns the average number of pages across all books in the database.

- **get_largest_book_name()**:
This method retrieves the name of the book with the highest number of pages from the database.

- **close_connection()**:
This method closes the SQLite database connection.
