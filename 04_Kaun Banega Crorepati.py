import random

def generate_question():
    """Generate a random question."""
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    return num1, num2

def verify():
    """Verify if the user's answer is correct."""
    num1, num2 = generate_question()
    correct_answer = num1 + num2
    user_answer = int(input(f"What is the sum of {num1} and {num2}? "))
    if user_answer == correct_answer:
        a = input("Enter Your Name for participation: ")
        c = a.title()
        print(c, end=", ")
        print("Use \"A, B, C, D\" for answering")
        print("You will win 5 crore Rs. for every correct answer")

        input("Press Enter to Proceed Further")


        ques1 = "Q1 : How much is 1 Astronomical Unit(AU)?"
        ques2 = "Q2 : What kind of star is our Sun?"
        ques3 = "Q3 : How much time does the light take to reach on Earth at its closest point?"
        ques4 = "Q4 : How much is 1 light-year in kilometers?"
        ques5 = "Q5 : Where is asteroid belt situated?"
        ques6 = "Q6 : How many moons does Jupiter have?"
        ques7 = "Q7 : Which Black Hole is present in center of Milky Way Galaxy?"
        ques8 = "Q8 : When does Kilonova occurs, when ___________ collides?"
        ques9 = "Q9 : Which electromagnetic radiation have potential to eradicate life on Earth?"
        ques10 = "Q10 : In which constellation is the Rigel star present"


        def Answer(x):
            if x == answer:
                print("Congratulations!! You won 5 crore rs.")
            else:
                print("Better luck next time ")

        print(ques1)
        a = ['A = 150.52 million km', 'B = 176.27 million km', 'C = 100 million km', "D = 20 billion km"]
        print(a)
        print()
        ans = input("Enter answer: ")
        answer = "A"
        Answer(ans)
        if ans == "A":
            win = 5
        else:
            win = 0
        print()
        input("press Enter for next question")
        print()
        print(ques2)
        b = ['A = O type', 'B = A type', 'C = G type', 'D = M type']
        print(b)
        print()
        ans = input("Enter answer: ")
        answer = "C"
        Answer(ans)
        if ans == "C":
            win2 = 5
        else:
            win2 = 0
        print()
        input("press Enter for next question")
        print()
        print(ques3)
        c = ['A = 510 seconds', 'B = 490 seconds', 'C = 310 seconds', 'D = 600 seconds']
        print(c)
        print()
        ans = input("Enter answer: ")
        answer = "B"
        Answer(ans)
        if ans == "B":
            win3 = 5
        else:
            win3 = 0
        print()
        input("press Enter for next question")
        print()
        print(ques4)
        d = ['A = 9.5 trillion km', 'B = 450 million km', 'C = 6.3 trillion km', 'D = 95.2 million km']
        print(d)
        print()
        ans = input("Enter answer: ")
        answer = "A"
        Answer(ans)
        if ans == "A":
            win4 = 5
        else:
            win4 = 0
        print()
        input("press Enter for next question")
        print()
        print(ques5)
        e = ['A = between Jupiter and Saturn', 'B = between Earth and Mars', 'C = Between Neptune and Uranus', 'D = between Mars and Jupiter']
        print(e)
        print()
        ans = input("Enter answer: ")
        answer = "D"
        Answer(ans)
        if ans == "D":
            win5 = 5
        else:
            win5 = 0
        print()
        input("press Enter for next question")
        print()
        print(ques6)
        f = ['A = 87', 'B = 96', 'C = 95', 'D = 85']
        print(f)
        print()
        ans = input("Enter answer: ")
        answer = "C"
        Answer(ans)
        if ans == "C":
            win6 = 5
        else:
            win6 = 0
        print()
        input("press Enter for next question")
        print()
        print(ques7)
        g = ['A = TON 618', 'B = Sagittarius A', 'C = Messier 60', 'D = Phoenix A']
        print(g)
        print()
        ans = input("Enter answer: ")
        answer = "B"
        Answer(ans)
        if ans == "B":
            win7 = 5
        else:
            win7 = 0
        print()
        input("press Enter for next question")
        print()
        print(ques8)
        h = ['A = two Neutron Star', 'B = two supergiant stars', 'C = two white dwarf stars', 'D = two Planets']
        print(h)
        print()
        ans = input("Enter answer: ")
        answer = "A"
        Answer(ans)
        if ans == "A":
            win8 = 5
        else:
            win8 = 0
        print()
        input("press Enter for next question")
        print()
        print(ques9)
        i = ['A = X-rays', 'B = UV rays', 'C = Gamma rays', 'D = IR rays']
        print(i)
        print()
        ans = input("Enter answer: ")
        answer = "C"
        Answer(ans)
        if ans == "C":
            win9 = 5
        else:
            win9 = 0
        print()
        input("press Enter for next question")
        print()
        print(ques10)
        j = ['A = Ursa Major', 'B = Orion', 'C = Cassiopeia', 'D = Aries']
        print(j)
        print()
        ans = input("Enter answer: ")
        answer = "B"
        Answer(ans)
        if ans == "B":
            win10 = 5
        else:
            win10 = 0
        print()
        input("press Enter to view your Earning")
        print()
        a = win + win2 + win3 + win4 + win5 + win6 + win7 + win8 + win9 + win10
        print("The total amount you won is ", a, "Crore")
        input("Press Enter to EXIT the game")

    else:
        print("Incorrect answer! Please try again.")

if __name__ == "__main__":
    verify()

input("Press any button to exit.")

# questions = [
#         ["Q1 : How much is 1 Astronomical Unit(AU)?"],
#         ["Q2 : What kind of star is our Sun?"],
#         ["Q3 : How much time does the light take to reach on Earth at its closest point?"],
#         ["Q4 : How much is 1 light-year in kilometers?"],
#         ["Q5 : Where is asteroid belt situated?"],
#         ["Q6 : How many moons does Jupiter have?"],
#         ["Q7 : Which Black Hole is present in center of Milky Way Galaxy?"],
#         ["Q8 : When does Kilonova occurs, when ___________ collides?"],
#         ["Q9 : Which electromagnetic radiation have potential to eradicate life on Earth?"],
#         ["Q10 : In which constellation is the Rigel star present"],
# ]

# for i in range(0, len(questions)):
#     question = questions[i]
#     print(question)

'''A better option'''