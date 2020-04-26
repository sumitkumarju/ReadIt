import csv
from ReadIt.models import book
from ReadIt  import app,db


def main():
    f = open("books.csv")
    reader = csv.reader(f)
    for isbn, title, author, year in reader:
        book = Book(isbn=isbn, title=title, author=author, year=year)
        db.session.add(book)
        print(f"Added book {title} by {author} .")

    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()
