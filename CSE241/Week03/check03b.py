class Complex:

    def __init__(self):
        self.real = 0
        self.imaginary = 0

    def prompt_values(self):
        self.real = int(input("\nPlease enter the real part: "))
        self.imaginary = int(input("Please enter the imaginary part: "))
    

    def display_complex(self):
        print(self.real," + ", self.imaginary,"i", sep= "")


def main():
    complex1= Complex()
    complex2= Complex()

    print("The values are:")
    complex1.display_complex()
    complex2.display_complex()


    complex1.prompt_values()
    complex2.prompt_values()

    print("\nThe values are:")
    complex1.display_complex()
    complex2.display_complex()

if __name__ == "__main__":
    main()



