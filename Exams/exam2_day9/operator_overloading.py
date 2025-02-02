class Book:
    def __init__(self,title):
        self.title=title

    def __add__(self,other):
        return Book(self.title+" & "+other.title)

    def display(self):
        print(f"Book Series: {self.title}")

b1=Book("Naruto")
b2=Book("One Piece")

series=b1+b2
series.display() 




