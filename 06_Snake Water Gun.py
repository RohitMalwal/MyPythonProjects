import random as r
print("snake beats water")
print("water beats gun")
print("gun beats snake")
winsY = 0
winsC = 0
tie = 0
print("you will get only 10 chances, the one who wins more will win finally")
def game():
    l = ["snake", "water", "gun"]
    a = r.choice(l)
    inp = input("enter snake, water and gun:\n")
    global winsC
    global winsY
    global tie
    if inp==a:
        print(f"computer chooses \'{a}\' and you chooses \'{inp}\' so \'MATCH TIES\' ", f"{10 - i} chances left")
        tie += 1
    elif inp=="snake" and a=="water":
        #snake beats water
        print(f"computer chooses \'{a}\' and you chooses \'{inp}\' so \'YOU WIN\' ", f"{10 - i} chances left")
        winsY += 1
    elif inp=="snake" and a=="gun":
        #gun beats snake
        print(f"computer chooses \'{a}\' and you chooses \'{inp}\' so \'YOU LOSE\' ", f"{10 - i} chances left")
        winsC += 1
    elif inp=="water" and a=="snake":
        #snake beats water
        print(f"computer chooses \'{a}\' and you chooses \'{inp}\' so \'YOU LOSE\' ", f"{10 - i} chances left")
        winsC += 1
    elif inp=="water" and a=="gun":
        #water beats gun
        print(f"computer chooses \'{a}\' and you chooses \'{inp}\' so \'YOU WIN\' ", f"{10 - i} chances left")
        winsY += 1
    elif inp=="gun" and a=="snake":
        #gun beats snake
        print(f"computer chooses \'{a}\' and you chooses \'{inp}\' so \'YOU WIN\' ", f"{10 - i} chances left")
        winsY += 1
    elif inp=="gun" and a=="water":
        #water beats gun
        print(f"computer chooses \'{a}\' and you chooses \'{inp}\' so \'YOU LOSE\' ", f"{10 - i} chances left")
        winsC += 1
    else:
        print("ERROR: input must be 'sanke', 'water' or 'gun' ")
        exit()
        
i = 0
while (i<10):
    i += 1
    game()
print()
print(f"you wins {winsY} times and loses {(10 - tie) - winsY} times")
print(f"Computer wins {winsC} times and loses {(10 - tie) - winsC} times")
print(f"match ties {tie} times")
print()
if winsC > winsY:
    print("Better luck next time, You have \'LOST\' your game.")
if winsC < winsY:
     print("Congratulations, Finally you have \'WON\' your game.")
elif winsC == winsY:
    print("Match tied")
else:
    pass
print(input("press ENTER to exit"))