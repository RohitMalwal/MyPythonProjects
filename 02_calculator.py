## a command line utilty of calculations

'''
to use this command line utility, open this file in cmd or powershell, or according to your OS

write command like this to calculate the the values:-

--> after opening this file do not click enter start writing after the path of the file
--> --x (first number) --o (operator) --y (second number)

'''

import argparse

def calc(a, b):
    if args.o == '+':
        return a+b
    elif args.o == '-':
        return a-b
    elif args.o == '*':
        return a*b
    elif args.o == '/':
        return a/b
    elif args.o == '**':
        return a**b
    else:
        return 'enter valid operator'


argument = argparse.ArgumentParser()

argument.add_argument('--x', type=int, required=True)
argument.add_argument('--o', type=str, required=True)
argument.add_argument('--y', type=int, required=True)

args = argument.parse_args()

result = calc(args.x, args.y)
print(result)
