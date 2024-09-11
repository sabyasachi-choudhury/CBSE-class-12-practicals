import mysql.connector

connection = mysql.connector.connect(host='localhost', user='root', passwd='Sabya19sachi05', database='cs_practicals')
cursor = connection.cursor()

# Inserting records
data = [
["ADS014", "Kim Jong", "M", "Seoul", "2007/01/05", "Cancer", "1987/11/12"],
["ADS015", "Huang Dong", "F", "Ulsan", "2008/08/01", "Typhoid", "1987/10/22"],
["ADS016", "Ban Moon", "M", "Busan", "2004/04/07", "Pneumonia", "1987/04/13"],
["ADS017", "Jim In", "F", "Seoul", "2007/11/11", "Rickets", "1997/01/01"],
["ADS018", "Nah Gon", "F", "Pyeongyang", "2007/02/22", "Bronchitis", "1989/11/02"]
    ]

for row in data:
    cursor.execute("insert into patient values ('%s', '%s', '%s', '%s', '%s', '%s', '%s');"%tuple(row))

connection.commit()

#Sort and display
print("Patients sorted by Name")
cursor.execute("select * from patient ORDER BY `Patient Name`;")

for row in cursor.fetchall():
    print(row)

print()

#Select Female Patients
print("Female patients")
cursor.execute("select * from patient where Gender = 'F';")
for row in cursor.fetchall():
    print(row)

print()

#select patients born in april of 1987
cursor.execute("select * from patient where `Date of Birth` between '1987/04/01' and '1987/04/30';")
print("Patients born in April 1987")
for row in cursor.fetchall():
    print(row)


