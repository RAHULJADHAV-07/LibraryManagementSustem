from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)
BOOKS_FILE = 'books.csv'

def read_books():
    """Reads books from the CSV file."""
    try:
        with open(BOOKS_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def write_books(books):
    """Writes books to the CSV file."""
    with open(BOOKS_FILE, mode='w', newline='') as file:
        fieldnames = ['ID', 'Title', 'Author', 'Copies']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Displays the home page with a list of books and search functionality."""
    books = read_books()
    search_query = request.form.get('search', '').lower()

    if search_query:
        books = [book for book in books if search_query in book['Title'].lower() or search_query in book['Author'].lower()]

    return render_template('index.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    """Allows the user to add a new book."""
    if request.method == 'POST':
        book_id = request.form['id']
        title = request.form['title']
        author = request.form['author']
        copies = request.form['copies']

        books = read_books()
        books.append({'ID': book_id, 'Title': title, 'Author': author, 'Copies': copies})
        write_books(books)

        return redirect(url_for('index'))

    return render_template('add_book.html')

@app.route('/remove', methods=['GET', 'POST'])
def remove_book():
    """Allows the user to remove a book."""
    if request.method == 'POST':
        book_id = request.form['id']
        books = read_books()
        books = [book for book in books if book['ID'] != book_id]
        write_books(books)
        return redirect(url_for('index'))

    return render_template('remove_book.html')

@app.route('/borrow', methods=['GET', 'POST'])
def borrow_book():
    """Allows the user to borrow a book."""
    if request.method == 'POST':
        book_id = request.form['id']
        books = read_books()

        for book in books:
            if book['ID'] == book_id and int(book['Copies']) > 0:
                book['Copies'] = str(int(book['Copies']) - 1)
                write_books(books)
                return redirect(url_for('index'))

        return "Book not available or out of stock."

    return render_template('borrow_book.html')

@app.route('/return', methods=['GET', 'POST'])
def return_book():
    """Allows the user to return a book."""
    if request.method == 'POST':
        book_id = request.form['id']
        books = read_books()

        for book in books:
            if book['ID'] == book_id:
                book['Copies'] = str(int(book['Copies']) + 1)
                write_books(books)
                return redirect(url_for('index'))

        return "Invalid Book ID."

    return render_template('return_book.html')

if __name__ == '__main__':
    app.run(debug=True)
