class Person():

    def __init__(self):

        self.name= "anonnymous"
        self.birthyear= "unknown"

    def display(self):
        print("{} ({})" .format( self.name, self.birthyear))

class Book():

    def __init__(self):

        self.title="untitled"
        self.author= Person()
        self.publisher="unpublished"

    def display(self):
        print(f"{self.title}")
        print("Publisher: ")
        print(f"{self.publisher}")
        print("Author")
        self.author.display()

def main():

    newbook = Book()
    author= Person()
    newbook.display()
    print()

    print("Please enter the following: ")
    author.name=input("Name:")
    author.birthyear= input("Year: ")
    newbook.title=input("Title: ")
    newbook.publisher=input("Publisher: ")

    newbook.display()
    


main()





    
        