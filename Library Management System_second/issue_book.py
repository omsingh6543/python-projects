from utils import books, issue_books
import datetime

def issue():
    
    book_name = input("Enter book name: ").upper()

    if book_name in books:
        student_name = input("Enter your name: ").upper()
        roll_no = input("Enter your roll number: ").upper()
        course = input("Enter course name: ").upper()
        section = input("Enter your section: ").upper()
        issue_date = datetime.datetime.now().date()
        due_date = issue_date + datetime.timedelta(days = 7)
        
    if book_name in books:
        
        books.remove(book_name)
        
        issue_books[book_name] = {"Book_name": book_name,
                       "Student_name": student_name, 
                       "Roll number": roll_no, 
                       "Course_name": course, 
                       "Section": section,
                       "Date of issueing book": issue_date,
                       "Estimate return":due_date}
        
        print(f"Book {issue_books[book_name]["Book_name"]} issued to {issue_books[book_name]["Student_name"]} successfully")

    else:
        print("Book not available")
    

