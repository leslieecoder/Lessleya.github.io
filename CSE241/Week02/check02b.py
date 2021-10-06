
fileName = input("Enter file: ")
doc= open(fileName, "r")

number_lines= 0
number_words= 0


for line in doc:
    line = line.strip("\n")

    words = line.split()
    number_lines += 1
    number_words += len(words)
    

doc.close()

print(f"The file contains {number_lines} lines and {number_words} words.")
