num = (input("Enter the number: "))
number = num.lstrip("0")

ones = [
    "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"
]
teens = [
    "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", 
    "Seventeen", "Eighteen", "Nineteen"
]
tens = [
    "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", 
    "Eighty", "Ninety"
]
thousands = ["", "Thousand"]
hundreds = ["", "Hundred"]

if len(number) == 1 and number == "0":
    print("Zero", end=" ")

# identify one digit number
def OneDigit():
    if len(number) == 1:
        print(ones[int(number)], end=" ")

# identify teens
def Teen():
     if len(number) == 2 and number[0] == "1" :
        print(teens[int(number[1])], end=" ")

# identify tens
def Tens():
     if len(number) == 2 and number[1] == "0":
        print(tens[int(number[0])], end=" ")

# identify two digits
def TwoDigits():
    if len(number) == 2 and number[0] != "1" and number[1] != "0":
        print(f"{tens[int(number[0])]} {ones[int(number[1])]}", end=" ")

# identify hundreds
def Hundreds():
    if len(number) == 3:
        if number[1:] == "0"*(len(number)-1):
            print(f"{ones[int(number[0])]} {hundreds[1]}", end=" ")
        elif number[1] == "1":
            print(f"{ones[int(number[0])]} {hundreds[1]} and {teens[int(number[2])]}", end=" ")
        elif number[1] == "0":
            print(f"{ones[int(number[0])]} {hundreds[1]} and {ones[int(number[2])]}", end=" ")
        else:
            print(f"{ones[int(number[0])]} {hundreds[1]} and {tens[int(number[1])]} {ones[int(number[2])]}", end=" ")
    
# identify thousands
def Thousands():
    if len(number) == 4:
        if number[1:] == "0"*(len(number) - 1):
            print(f"{ones[int(number[0])]} {thousands[1]}", end=" ")
        elif number[2] == "1":
            print(f"{ones[int(number[0])]} {thousands[1]} {ones[int(number[1])]} {hundreds[1]} and\
 {teens[int(number[3])]}", end=" ")
        elif number[1] == "0":
            print(f"{ones[int(number[0])]} {thousands[1]} and {tens[int(number[2])]} {ones[int(number[3])]}", end=" ")
        else:
            print(f"{ones[int(number[0])]} {thousands[1]} {ones[int(number[1])]} {hundreds[1]} and\
 {tens[int(number[2])]} {ones[int(number[3])]}", end=" ")

# identify ten thousands
def TenThousands():
    if len(number) == 5:
        pass

if __name__ == "__main__":
    if num[0:] == "0"*len(num):
        print("Zero")
    else:
        OneDigit()
        Teen()
        Tens()
        TwoDigits()
        Hundreds()
        Thousands()
        TenThousands()