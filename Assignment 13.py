details = [
    ["Siddarth", "Delux"],
    ["Rahul","Standard"],
    ['Jerry', "Delux"]
    ]

stack = []

def push_cust():
    for elem in details:
        if elem[1] == 'Delux':
            stack.insert(0, elem[0])

def pop_cust():
    while stack:
        print(stack.pop(0))
    print("Underflow")

def display_status():
    for elem in stack:
        print(elem)

s = """
Pick an option
1. push
2. pop
3. display
4. exit
"""

print(s)
x = int(input("Enter option: "))
while x != 4:
    if x == 1:
        push_cust()
    elif x == 2:
        pop_cust()
    elif x == 3:
        display_status()
    else:
        print("choose valid option")

    x = int(input("Enter next option: "))
