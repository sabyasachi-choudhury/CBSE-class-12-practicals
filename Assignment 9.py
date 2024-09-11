import pickle

"""ASsuming member number is unique"""

def member_name(num):
    found = False
    with open("Member.dat", "rb") as file:
        while True:
            try:
                data = pickle.load(file)
                if data['MemberNo'] == num:
                    print(data['Name'])
                    found = True
                    break
            except:
                break
        if not found:
            print("No such member")

def del_sales():
    new_data = []
    with open("Member.dat", "rb") as file:
        while True:
            try:
                data = pickle.load(file)
                if data['Department'].lower() != 'sales':
                    new_data.append(data)
            except:
                break
    with open("Member.dat", "wb") as file:
        for elem in new_data:
            pickle.dump(elem, file)

def display():
     with open("Member.dat", "rb") as file:
        while True:
            try:
                print(pickle.load(file))
            except:
                break

def new_file(elems):
    with open("Member.dat", "ab") as file:
        for row in elems:
            pickle.dump(row, file)

print("Choose options")
print("1: Update file")
print("2: Find name by member number")
print("3: Remove all sales members")
print("4: Display all members")
print("5: Exit Program")
choice = int(input("Enter choice: "))
while choice != 5:
    
    if choice == 1:
        print("Enter data in following format")
        print("<Member number 1>,<Name 1>,<Department 1>")
        print("<Member number 2>,<Name 2>,<Department 2>")
        print("Keep entering until data completed, at which point enter '0'")
        x = input()
        data = []
        while x != '0':
            x = x.split(',')
            data.append({'MemberNo': int(x[0]), 'Name': x[1], 'Department': x[2]})
            x = input()
        new_file(data)

    elif choice == 2:
        x = int(input('Enter member number: '))
        member_name(x)

    elif choice == 3:
        del_sales()

    elif choice == 4:
        display()

    elif choice == 5:
        break

    choice = int(input("Enter next choice: "))
