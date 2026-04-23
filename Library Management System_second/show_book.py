from utils import books, issue_books

def show():
    print(f"Available Books: {books if books else 'None'}")

    if issue_books:
        print("Issued Books:")
        for book, info in issue_books.items():
            print(f"{book} issued to {info["student_name"]}")
    else:
        print("No books are currently issued.")