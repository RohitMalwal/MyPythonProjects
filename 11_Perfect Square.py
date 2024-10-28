import random as r
from math import sqrt
import time
# numbers = list(range(1,101))

# a= r.randint(1, 100)
# b= r.randint(1, 100)
# c= r.randint(1, 100)

# x = sqrt((a*a)+(b*b)+(c*c))

# print(a,b,c,x)

list_ = list(range(1, 1001))
# print(type(float(list[12])))

while True:
    a= r.randint(1, 100)
    b= r.randint(1, 100)
    c= r.randint(1, 100)
    x = sqrt((a*a)+(b*b)+(c*c))
    for item in list_:
        if x == float(item):
            print(a, b, c)
            print(x)
            time.sleep(1)

    # for item in list:
    #     if x == float(item):
    #         break