#Create a class for a Book that has the following member variables:
# title : string

# author : string

# publication_year : int

class Book():

    def __init__(self):
        self.title = ""
        self.author = ""
        self.publication_year = ""
    
    # In the base Book class, create a method prompt_book_info that prompts the user for the title, 
    # author, and publication_year

    def prompt_book_info(self):
        self.title = input("Title: ")
        self.author = input("Author: ")
        self.publication_year = int(input("Publication Year: "))

    # method display_book_info that displays the title, author, 
    # and publication year in the format: "Title (publication_year) by Author".

    def display_book_info(self):
        print(self.title,"(", self.author,")", self.publication_year)

# create a class for a TextBook that extends a Book and adds the following member variable:
# subject : string

class TextBook(Book):

            
    def __init__(self, title, author, publication_year):

                self.subject = ""
                # invoking the __init__ of the parent class 
                Book.__init__(self, title, author, publication_year) 

#In the TextBook class, create methods prompt_subject and display_subject that prompt
#  and display the subject of the book.

    def prompt_subject(self):
        self.subject = input("Subject: ")


    def display_subject(self):
        print(self.subject)

# create a class for a PictureBook that that extends a Book and adds the following member variable:
# illustrator : string

class PictureBook(Book):
    def __init__(self, title, author, publication_year):
        self.illustrator = ""
        # invoking the __init__ of the parent class 
        Book.__init__(self, title, author, publication_year)

 #In the PictureBook class, create methods prompt_illustrator and display_illustrator that prompt
 #  and display the Illustrator of the book.   

    def prompt_illustrator(self):
        self.illustrator = input("Subject: ")

    def display_illustrator(self):
        print(self.illustrator)

def main():

#In main, first create a Book object and call the following methods:

    newBook = Book()


    newBook.prompt_book_info()

    newBook.display_book_info()

#Next, create a TextBook object and call the following methods:

    newTextBook = TextBook()

    newBook.prompt_book_info()

    newTextBook.prompt_subject()

    newBook.display_book_info()

    newTextBook.display_subject()
#Finally, create a PictureBook object and call the following methods:
    pictureBook = PictureBook() 

    newBook.prompt_book_info()

    pictureBook.prompt_illustrator()

    newBook.display_book_info()

    pictureBook.display_illustrator()


if __name__ == "__main__":
    main()













