class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []
        
    @property
    def showinfo(self):
        print(f"Total books in library : {self.noBooks}\n")
        for book in self.books:
            print(book)

    @showinfo.setter
    def addBook(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def check(self):
        if self.noBooks == len(self.books):
            print(f"\nLooks Good")
        else:
            print("There is an ERROR in you books counting")
    
a = Library()
a.addBook = 'Harry Potter'
a.addBook = 'Learn Programming in Python'
a.addBook = 'The Art of Seduction'
a.showinfo
a.check()