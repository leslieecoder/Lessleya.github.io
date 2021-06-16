	# Example 1

def main():
    # Read the contents of a text file
    # named provences.txt into a list.
    provinces = read_list("provinces.txt")

    # Print the entire list.
    print(text_list)

     # Remove the first element from the list.
    provinces.pop(0)
    #print(provinces)

    # Remove the last element from the list.
    provinces.pop()
    #print(provinces)
  
    # Replace all occurrrences of "AB" with "Alberta".
    for i in range(len(provinces)):
        if provinces[i] == "AB":
            provinces[i] = "Alberta"
    #print(provinces)

    # Call the list.count method which will count the
    # number of times that Alberta appears in the list.
    count = provinces.count("Alberta")

    print()
    print(f"Alberta occurs {count} times in the modified list.")

def read_list(filename):
    """Read the contents of a text file into a list and
    return the list. Each element in the list will contain
    one line of text from the text file.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    # Create an empty list named text_list.
    text_list = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "rt") as text_file:

        # Read the contents of the text
        # file one line at a time.
        for line in text_file:

            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()

            # Append the clean line of text
            # onto the end of the list.
            text_list.append(clean_line)

    # Return the list that contains the lines of text.
    return text_list


# Call main to start this program.
if __name__ == "__main__":
    main()