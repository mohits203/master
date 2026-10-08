class Book:
    
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def displayDetails(self):
        print(f"Title of the book is : {self.title} and author is : {self.author}")

class EBook(Book):

    def __init__(self, title: str, author: str, fileSize: float):
        super().__init__(title, author)
        self.fileSize = fileSize

    
    def displayDetails(self):
        print(f"Title of the book is : {self.title} and author is : {self.author} and the file size is : {self.fileSize} MB.")


title = input("Title of the book : ")
author = input("Author of the book : ")
fileSize = float(input("Size of the eBook file in MB : "))

obj = EBook(title, author, fileSize)
obj.displayDetails()
