data = {
    'Santro': 'Hyundai',
    "Nexon": "TATA",
    "Safari": "tata"
    }

car = []

def push(vehicle):
    for elem in vehicle:
        if vehicle[elem].lower() == 'tata':
            car.insert(0, elem)

def pop():
    if car:
        print(car.pop(0))
    else:
        print("Underflow")

def count():
    if len(car) == 0:
        print("Underflow")
    else:
        print(len(car))

def display():
    for elem in car:
        print(elem)

s = """
Pick an option from below
1. PUSH
2. POP
3. DISPLAY
4. COUNT
5. EXIT
"""

x = int(input("Enter option: "))
while x != 5:
    if x == 1:
        push(data)
    elif x == 2:
        pop()
    elif x == 3:
        count()
    elif x == 4:
        display()
    else:
        print("Invalid option")

    x = int(input("enter next option: "))
    
