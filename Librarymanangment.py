#library managment system
class Book:
    def __init__(self,title,author,available):
        self.title=title
        self.author=author
        self.available=available
    def display_info(self):
        print(f"{self.title} is written by {self.author} ")
class Library:
    def __init__(self):
        self.book=[Book("python guide", "ali", True),
        Book("java guide", "ahmed", False)]
    
    def add_book(self):
        title=input("enter title of book: ")
        author=input("enter author of book: ")
        book1= Book(title,author,True)
        self.book.append(book1)
        print(f"{title} written by {author} is added successfully.")
    def display_book(self):
        if not self.book:
            print("no book is available")
        else:
            for book in self.book:
                book.display_info()
    def borrow_book(self):

        title=input('enter title: ')
        for book in self.book:
            if book.title == title and book.available:
                print(f"You borrowed '{book.title}'.")
                book.available = False
                return
        print("Book not available.")

    
    def run(self):
        while True:
            print("press 1 to add book")
            print("press 2 to display books")
            print("press 3 to borrow book")
            print("press 4 for exit")
            choice=int(input("enter your choice: "))
            if choice==1:
                self.add_book()
            elif choice==2:
                self.display_book()
            elif choice==3:
                self.borrow_book()
            elif choice==4:
                print("thank you for using....")
                break
 
library1=Library()
library1.run()


