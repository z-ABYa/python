class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.no_of_books +=1

    def showInfo(self):
        print(f"The Library has {self.no_of_books}. The Books are:")
        for book in self.books:
            print(book)

library = Library()
library.addBook("B1")
library.addBook("B2")
library.addBook("B3")
library.showInfo()
