with open("details.txt", "r") as file:
    bad, good = [], []
    for string in file.readlines():
        at = string.index("@")
        product = string[:at]
        code = string[at+1:-1]
        if code[:3] != product[:3]:
            bad.append(code)
        else:
            for char in code:
                if char in "1234567890":
                    good.append(code)
                    break
            if good[-1] != code:
                bad.append(code)

with open("Errors.txt", "w") as file:
    print("Bad codes")
    for elem in bad:
        print(elem)
        file.write(elem + "\n")

print()

with open("Finalcodes.txt", "w") as file:
    print("Good codes")
    for elem in good:
        print(elem)
        file.write(elem + "\n")
    
