#Create a class for a Student, that contains a first name, a last name, and an id

class Student:

    def __int__(self):

        self.fname=""
        self.lname=""
        self.id=0

def prompt_student():
    student = Student()
    student.fname = input("Please enter your first name: ")
    student.lname = input("Please enter your last name: ")
    student.id= int(input("Please enter your id number: "))
    return student

def display_student(student):
    print("Your information:")
    print(student.id,"-", student.fname, student.lname)


def main():
    user = prompt_student()
    print()
    display_student(user)
if __name__ == "__main__":
    main()


