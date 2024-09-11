data = [
    ["Gurdas", "99999999999", "Goa"],
    ["Julee", "88888888888", "Mumbai"],
    ["Murugan", "77777777777", "Cochin"],
    ["Ashmit", "10101010101", "Goa"]
    ]

status = []

def push():
    for elem in data:
        if elem[-1].lower() == 'goa':
            status.insert(0, elem)

def pop():
    while status:
        print(status.pop(0))
    print("Underflow")


s = """"
Pick an option from the following
1. PUSH
2. POP
3. EXIT
"""
x = int(input("Enter option: "))
while x != 3:
    if x == 1:
        push()
    elif x == 2:
        pop()
    else:
        print("Invalid option")

    x = int(input("Enter next option: "))
