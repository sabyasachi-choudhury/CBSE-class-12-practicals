"""ASsignment 4"""

pupilAttendance = [
    ["Faroukh" , "Salah" , 70],
    ["Kelvin", "Glintode" , 85],
    ["Lara" , "Godfrey" , 90],
    ["Amara" , "Grzinski" , 70],
    ["Aaron" , "Grimshaw" , 90],
    ["Farihaa" , "Mohan" , 95],
    ["Taz" , "Grimstow" , 60],
    ["Ali" , "Aisha" , 95],
    ["Charlene" , "Hall" ,85],
    ["Asra" , "Ashiq" , 90],
    ["Sadia" , "Bhatti" , 65],
    ["Ria" , "Hall" , 90],
    ["Fernado" , "Askabat" , 60],
    ["Richard" , "Hawkins" , 80],
    ["Siyao" , "Wang" , 60],
    ["Marketta" , "Hosier" , 100]
]

option = 0
print("Attendance menu options")
print("1 - Display names of low attendance")
print("2 - Display names of high attendance")
option = int(input("Enter option number: "))

def low_attendance():
    i = 0
    for student in pupilAttendance:
        if student[2] < 75:
            print(f"{student[0]} {student[1]}")
            i += 1
    print(f"\n{i} students have attendance below 75%")

def high_attendance():
    i = 0
    for student in pupilAttendance:
        if student[2] >= 90:
            print(f"{student[0]} {student[1]}")
            i += 1
    print(f"\n{i} students have attendance above or equal to 90%")

if option == 1:
    low_attendance()
elif option == 2:
    high_attendance()
else:
    print("Please enter a valid option")
