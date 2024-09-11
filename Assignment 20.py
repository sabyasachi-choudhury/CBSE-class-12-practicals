import mysql.connector

connection = mysql.connector.connect(host='localhost', user='root', passwd='Sabya19sachi05', database='cs_practicals')
cursor = connection.cursor()

# Inserting dummy records
#data = [
 #   ["Mr", '19281', 'Sushil', 'Kumar', 'Marketing', 1000000, '2010/05/19', 'M', 'Senior Analyst'],
  #  ["Mr", '29381', 'Prashant', 'Kumar', 'Engineering', 200000, '2018/05/19', 'M', 'Junior Engineer'],
   # ["Mrs", '22839', 'Manika', 'Rawat', 'Sales', 1200000, '2020/05/19', 'F', 'Senior Manager'],
    #["Miss", '00927', 'Priyanak', 'Arora', 'Sales', 200000, '2020/05/19', 'F', 'Junior Analyst'],
    #["Mr", '94712', 'Ashish', 'Nehra', 'RnD', 2000000, '2020/05/19', 'M', 'Chief'],
    #["Mrs", '24774', 'Preeti', 'Arora', 'Engineering', 2500000, '2010/05/19', 'F', 'General Manager'],
    #["Mrs", '66649', 'Sushma', 'Prasad', 'Marketing', 1900000, '2015/05/19', 'F', 'Senior Analyst']
    #]

#for row in data:
 #   cursor.execute("insert into emp values ('%s', '%s', '%s', '%s', '%s', %s, '%s', '%s', '%s');"%tuple(row))

#connection.commit()

#connection.close()


## Prompts to help make usage easier
prompt = """
Choose what you want to do

1 - Display all records
2 - Read a record by employee number
3 - Add a new record
4 - Delete a record by employee number
5 - Update an existing record
0 - Exit program
"""

prompt2 = """
Enter the following details in order, separated by commas.

Title, employee number, first name, last name, department, salary, date of joining(YYYY/MM/DD), gender (M or F), Designation

Example
Mr,29373,Sushil,Kumar,Marketing,10000,2010/04/19,M,Senior Analyst
"""

prompt3 = """
Pick the fields you wish to update

Fields available:
1: Title
2: Employee Number
3: First Name
4: Last Name
5: Department
6: Salary
7: Date of Joinint
8: Gender
9: Designation

Input fields you wish to update as the corresponding in single line, separated by commas.
Eg: 1,3,4,8
"""

field_dict = {
        '1': 'title',
        '2': 'empno',
        '3': 'fname',
        '4': 'lname',
        '5': 'dept',
        '6': 'sal',
        '7': 'doj',
        '8': 'gender',
        '9': 'desig'
    }

#Main Interface Loop
while True:
    
    print(prompt)
    choice = int(input("Enter number of what you want to do: "))

    #Choice 1 code: display full table
    if choice == 1:
        cursor.execute("select * from emp;")
        for row in cursor.fetchall():
            print(row)
        print()

    #Choice 2 code: find specific record by EmpNO
    elif choice == 2:
        num = input("Enter unique 5 digit employee number: ").strip()
        cursor.execute("select * from emp where EmpNo = '%s';"%(num,))
        print(cursor.fetchone())

    #Choice 3 code: Insert new record
    elif choice == 3:
        print(prompt2)
        data = input().split(",")
        data[5] = int(data[5])
        cursor.execute("insert into emp values ('%s', '%s', '%s', '%s', '%s', %s, '%s', '%s', '%s');"%tuple(data))
        connection.commit()
        print("New record")
        cursor.execute(f"select * from emp where empno={data[1]};")

    #Choice 4 code: Delete record by EmpNo
    elif choice == 4:
        num = input("Enter employee number to delete: ").strip()
        cursor.execute("delete from emp where EmpNo = '%s';"%(num,))
        connection.commit()
        print("Record Deleted. Display all records to see change.")

    # Choice 5 code: Update record by EmpNo
    elif choice == 5:
        num = input("Enter employee number to update: ").strip()
        print(prompt3)
        fields = input().split(",")
        command = "update emp set"
        for f in fields:
            command += " " + field_dict[f] + " = "
            if f != '6':
                command += "'" + input(f"Enter new value for {f}: ") + "',"
            else:
                command += input(f"Enter new value for {f}: ") + ","

        command = command[:-1]
        command += f" where empno = '{num}';";
        print(command)
        cursor.execute(command)
        connection.commit()
        print("Data updated. Display all records to see change")

    # Choice 0 code: exit loop
    elif choice == 0:
        break;

    # Invalid choices
    else:
        print("Enter valid choice\n")