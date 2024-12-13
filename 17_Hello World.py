from random import choice
from time import sleep

letters_L = "abcdefghijklmnopqrstuvwxyz"
letters_U = letters_L.upper()
letters = letters_L + " " + letters_U

word = input("Enter the word you wanna create: ")
result = ""

for letter in word:
    while True:
        l = choice(letters)
        print(result+l)
        if l==letter:
            result += l
            break
        sleep(0.01)

input("Press ENTER to exit.")