class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        
    def display(self):
        print(f"Book title: {self.title}\nAuthor: {self.author}\nISBN number: {self.isbn}")
        
def get_input():
    title=input("Enter the Book title: ")
    author=input("Enter the Author name: ")
    isbn=input("isbn number is: ")
    
    return (title,author,isbn)

title,author,isbn=get_input()
val=Book(title,author,isbn)
val.display()


