def Calculator():
    a = float(input("Enter First Number: "))
    b = (input("Enter Operator: "))
    c = float(input("Enter Second Number: ")) 

    if (b == '+'):
        result = (a + c)
    elif (b == '-'):
        result = (a - c)
    elif (b == '*'):
        result = (a * c)
    elif (b == '/'):
        result = (a / c)
    elif (b == '**'):
        result = (a ** c)
    elif (b == '//'):
        result = (a//c)
    else:
        result = ("Invalid Operator")   

    print(result)   

while True:
    Calculator()

