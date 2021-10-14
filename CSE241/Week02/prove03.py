#a class is a container that holds something and you define what a container is. Every class has the same thing
#init method and a self function

class Robot:

    def __init__(self):
        self.XCoordinate = 10
        self.YCoordinate = 10
        self.FuelAmount = 100

    def move_left(self):
        if (self.FuelAmount<= 0):
            print("Insufficent fuel to perform action")
        else:
            self.FuelAmount-=5
            self.XCoordinate -=1
        return
    
    def move_right(self):
        if (self.FuelAmount<= 0):
            print("Insufficent fuel to perform action")
        else:
            self.FuelAmount-=5
            self.XCoordinate -=1
        return

    def move_up(self):
        if (self.FuelAmount<= 0):
            print("Insufficent fuel to perform action")
        else:
            self.FuelAmount-=5
            self.YCoordinate -=1
        return

    def move_down(self):
        if (self.FuelAmount<= 0):
            print("Insufficent fuel to perform action")
        else:
            self.FuelAmount-=5
            self.YCoordinate -=1
        return

    def display_currentstatus(self):
        print("({}, {}) - Fuel: {}" .format(self.XCoordinate, self.YCoordinate, self.FuelAmount))
        return

    def fire_laser(self):
        print("Pew! Pew!")
        self.FuelAmount -=15
        return

def main():

    currentRobot = Robot()
    command = ""
    while (command != "quit"):
        command = input("Enter command: ")
        if(command == "left"):
            currentRobot.move_left()
        elif(command == "right"):
            currentRobot.move_right()
        elif(command == "jump"):
            currentRobot.move_up()
        elif(command == "down"):
            currentRobot.move_down()
        elif(command == "fire"):
            currentRobot.fire_laser()
        elif(command == "status"):
            currentRobot.display_currentstatus()
        elif(command == "quit"):
            print("Goodbye")

if __name__ == "__main__":
    main()





    



