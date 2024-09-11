def emailcheck():
    writefile = open("Error.txt", "w")
    with open("Email.txt", "r") as file:
        for elem in file:
            if "@" not in elem:
                writefile.write(elem)
    writefile.close()

def countuk(filename):
    with open(filename, "r") as file:
        n = 0
        for elem in file.readlines():
            if elem[-3:-1] == "uk":
                n += 1
                print(elem[:-1])
        print(f"{n} emails ending with uk")

emailcheck()
countuk("Email.txt")
