class Rationalnum:

    def __init__(self):
        self.numerator= 0
        self.denominator= 0

    def display_number(self):
        print(self.numerator,"/",self.denominator, sep="")
    
    def display_decimal(self):
        print(self.numerator,"/",self.denominator, sep="")
        print(self.numerator / self.denominator)
        

    def prompt__number(self):
        self.numerator= int(input("Enter the numerator: "))
        self.denominator= int(input("Enter the denominator: "))

def main():

    rational= Rationalnum()

    rational.display_number()
    rational.prompt__number()
    rational.display_decimal()

if __name__ == "__main__":
    main()



   
