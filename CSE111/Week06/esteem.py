def main():
    print("This program is an implementation of the Rosenberg Self-Esteem Scale. This program will show you ten statements that you could possiblyapply to yourself. Please rate how much you agree with each of the statements by responding with one of these four letters:")
    print()
    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.")



    q1 = input("I feel that I am a person of worth, at least on an equal plane with others: ")
    a1 = positiveQ(q1)
    q2 =input("I feel that I have a number of good qualities: ")
    a2 = positiveQ(q2)
    q3 =input("All in all, I am inclined to feel that I am a failure: ")
    a3 = negativeQ(q3)
    q4=input("I am able to do things as well as most other people: ")
    a4 = positiveQ(q4)
    q5=input("It feel I do not have much to be proud of")
    a5 = negativeQ(q5)
    q6=input("I take a positive attitude toward myself: ")
    a6 = positiveQ(q6)
    q7=input("On the whole, I am satisfied with myself: ")
    a7 = positiveQ(q7)
    q8=input("I wish I could have more respect for myself: ")
    a8 = negativeQ(q8)
    q9=input("I certainly feel useless at times: ")
    a9 = negativeQ(q9)
    q10=input("At times I think I am no good at all: ")
    a10 = negativeQ(q10)

    final_score = compute_final_score(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10)
    print(f"Your score is {final_score}.")

    print("A score below 15 may indicate problematic low self-esteem.")

def positiveQ(q):

    if q == "D":
        answer = 0
    elif q == "d":
        answer = 1  
    elif q == "a":
        answer= 2
    elif q == "A":
        answer=3

    return answer

def negativeQ(q):

    if q == "D":
        answer = 3
    elif q == "d":
        answer = 2
    elif q == "a":
        answer= 1
    elif q == "A":
        answer=0

    return answer

def compute_final_score(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10):

    final = a1+a2+a3+a4+a5+a6+a7+a8+a9+a10

    return final

main()
    

