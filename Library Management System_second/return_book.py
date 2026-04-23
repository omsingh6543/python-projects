from utils import issue_books, books
from datetime import datetime


def fine(late_days):
    if late_days <= 0:
        return 0
    weeks = (late_days + 6) // 7
    fine = 0
    for week in range(1, weeks+1):
        fine += week*10
    return fine

def return_book():
    
    book_name = input("Enter book name: ").upper()
    
    if book_name in issue_books:
        
        details = issue_books[book_name]
        issue_date = details["Date of issueing book"]
        days_kept = (datetime.now().date() - issue_date).days
        late_days = days_kept - 7
        
        print("Fine Applied = $",fine(late_days))
        books.append(book_name)
        
        print("Book returned successfully")
        
    else:
        print("This book was not issued")