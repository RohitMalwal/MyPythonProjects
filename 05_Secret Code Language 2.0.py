def codex():
    code = input(":- ")
    words = code.split(" ")
    if (coding):
        # output="" 
        new = []
        for word in words:
            if len(word) >= 3:
                r1 = "fid"
                r2 = "kjd"
                output = r1+word[1:]+word[0]+r2
                new.append(output)
            else:
                # output = word[::-1]
                new.append(word[::-1])
        # print(output)
        print(" ".join(new))
    else:
        new = []
        for word in words:
            if len(word) >= 3:
                output = word[3:-3]
                output = output[-1]+output[:-1]
                new.append(output)
            else:
                # output = word[::-1]
                new.append(word[::-1])
        print(" ".join(new))
try:
    coding = int(input("type 1 for coding and 0 for decoding: "))
    if coding == 1 or coding == 0: 
        True if coding == 1 else False 
        codex()
    else:
        print("entered value should be 0 or 1")

except:
    print("entered value should be 0 or 1")

print(input("press ENTER to exit"))
