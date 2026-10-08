class Book:
    
    def __init__(self):
        self.title = input("Title of the book : ")
        self.author = input("Author of the book : ")

    def displayDetails(self):
        print(f"Title of the book is : {self.title} and author is : {self.author}")

class EBook(Book):

    def __init__(self):
        super().__init__()
        self.fileSize = float(input("Size of the eBook file in MB : "))

    
    def displayDetails(self):
        print(f"Title of the book is : {self.title} and author is : {self.author} and the file size is : {self.fileSize} MB.")



obj = EBook()
obj.displayDetails()
