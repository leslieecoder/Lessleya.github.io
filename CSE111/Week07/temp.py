#PRACTICING WITH DICTIONARIES AND LISTS

student = { "first_name": "Lesliee",
            "last_name": "Cruz",
            "phone": 2094962091,
            "i-number": 385898628,
            "address": "508 W 1st S" }



print(student["first_name"])

#A for loop in a dictionary returns a key

for item in student: 
    print(item)

for item in student: 
    print(student[item])    

for item in student: 
    print(f"{item}: {str(student[item])}")    