from collections import deque 

#Create a Song class that has member variables for a title and an artist.
# It should have a prompt function that asks the user for the title and artist,
#  and a display function that displays the title and the artist to the screen.

class Song:

    def __init__(self):

        self.title = ""
        self.artist= ""

    def prompt(self):
        self.title= input("Enter the title: ")
        self.artist= input("Enter the artist: ")

    def display(self):
        print(self.title)
        print(self.artist)
        
#Create a deque of songs for your playlist.

song = Song()
playlist = deque() 

#Set up a main loop that asks the user for one of the following options:

#Add new song to the end of the playlist.

#Insert a new song at the beginning of the playlist (so it will play next).

#Play a song (this should remove it from the playlist).

print("Option: ")
print("1. Insert a new song at the beginning of the playlist (so it will play next).")
print("2. Add new song to the end of the playlist.")
print("3. Play a song (this should remove it from the playlist).")
print("4. Quit")


selection = 0

while selection != 4:
    selection = input("Enter a selection: ")

#Implement each of the above actions. 
#For the ones that add a new song, it should prompt the user for the values,
#and then add the song to the play list.

    if selection == 1 or selection == 2:
        Song.prompt()

#When the user selects the option to play a song, it should be removed from the list.
#Then, display a message to the user, "Playing song:",
#followed by the title and the artist of the song that was just removed from the front of the playlist.

    








