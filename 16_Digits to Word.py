num = input("enter the number: ").lstrip("0")

def int_to_word(num):
    d = { 0 : 'Zero', 1 : 'One', 2 : 'Two', 3 : 'Three', 4 : 'Four', 5 : 'Five',
        6 : 'Six', 7 : 'Seven', 8 : 'Eight', 9 : 'Nine', 10 : 'Ten',
        11 : 'Eleven', 12 : 'Twelve', 13 : 'Thirteen', 14 : 'Fourteen',
        15 : 'Fifteen', 16 : 'Sixteen', 17 : 'Seventeen', 18 : 'Eighteen',
        19 : 'Nineteen', 20 : 'Twenty',
        30 : 'Thirty', 40 : 'Forty', 50 : 'Fifty', 60 : 'Sixty',
        70 : 'Seventy', 80 : 'Eighty', 90 : 'Ninety' }

    k = 1000
    m = k * k
    b = m * k
    t = b * k   

    number = int(num)

    try:
        assert int(number)>=0
    except AssertionError:
        return("Enter a valid positive number.")
    
    if (number) < 20:
        return (d[(number)])

    if (number) < 100:
        if (number) % 10 == 0:
            return (d[(number)])
        else:
            return (f"{d[(number) // 10 * 10]}-{d[(number) % 10]}")
    
    if (number) < k:
        if (number) % 100 == 0:
            return (f"{d[(number) // 100]} Hundred")
        else:
            return (f"{d[(number) // 100]} Hundred and {int_to_word(number % 100)}")
        
    if (number) < m:
        if (number) % k == 0:
            return (f"{int_to_word((number) // k)} Thousand")
        else:
            return (f"{int_to_word((number) // k)} Thousand, {int_to_word((number % k))}")
    
    if (number) < b:
        if (number) % m == 0:
            return (f"{int_to_word((number) // m)} Million")
        else:
            return (f"{int_to_word((number) // m)} Million, {int_to_word((number) % m)}")
    
    if (number) < t:
        if (number) % b == 0:
            return (f"{int_to_word((number) // b)} Billion")
        else:
            return (f"{int_to_word((number) // b)} Billion, {int_to_word((number) % b)}")
    
    if (number) > t:
        if (number) % t == 0:
            return (f"{int_to_word((number) // t)} Trillion")
        else:
            return (f"{int_to_word((number) // t)} Trillion, {int_to_word((number) % t)}")

if __name__=="__main__":
    result = int_to_word(num)
    if result:
        print(result)