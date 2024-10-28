def Encrypt():
    Code = input(":- ")
    A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Ai = "!)@(#*$&%^-=_+][}{:;<>,./?"
    Ai = A[::-1]
    a = A.swapcase()
    ai = a[::-1]
    # ai = Ai[::-1]

    converted_data = ""

    for i in range(0, len(Code)):
        if Code[i] in A:
            converted_data += Ai[A.index(Code[i])]    
        elif Code[i] in a:
            converted_data += ai[a.index(Code[i])]
        else:
            converted_data += " "
    return converted_data
while 1 > 0:
    x = Encrypt()
    print(x)
