import csv

filename = "PLANTS_STOCK.csv"

def display_all():
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for elem in reader:
            print(elem)

def add_plant():
    category = input("Enter plant category:")
    name = input("Enter plant name:")
    variety = input("Enter plant variety:")
    code = input("Enter plant code:")
    reference_id = input("Enter plant reference_id:")
    unit = input("Enter plant unit:")
    price = input("Enter plant price:")
    height = input("Enter plant height:")
    with open(filename, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([category, name, variety, code, reference_id, unit, price, height])

def search_id(ref):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        found = False
        for elem in reader:
            if elem[4] == ref:
                found = True
                print(elem)
                break
        if not found:
            print("ID not found")

def update_medium():
    new_data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for elem in reader:
            if elem[-1] == 'M':
                elem[-2] = str(float(elem[-2]) + 1)
            new_data.append(elem)

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(new_data)

def display_climber():
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for elem in reader:
            if elem[0].lower() == 'climber':
                print(elem)

def delete(ref):
    data = [elem for elem in csv.reader(open(filename, 'r')) if elem[4] != ref]
    with open(filename, 'w', newline='') as file:
        w = csv.writer(file)
        w.writerows(data)

print("Choose option from following")
s = """
1. Add a new plant
2. Search for a plant with its reference ID
3. Increase price of all medium plants by 1
4. Display all climbers
5. Delete a plant using its refID
6. Display all plants
7. Show options again
0. Exit program
"""

print(s)
x = int(input("Pick an Option: "))

while x != 0:
    if x == 1:
        add_plant()
    elif x == 2:
        search_id(input("Enter Reference ID: "))
    elif x == 3:
        update_medium()
    elif x == 4:
        display_climber()
    elif x == 5:
        delete(input("Enter Reference ID: "))
    elif x == 6:
        display_all()
    elif x == 7:
        print(s)
    else:
        print("No such Option")

    x = int(input("\n\nPick next option: "))
