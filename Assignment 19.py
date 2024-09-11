import mysql.connector

connection = mysql.connector.connect(host='localhost', user='root', passwd='Sabya19sachi05', database='cs_practicals')
cursor = connection.cursor()

# Inserting records
data = [
    ['SA1', 'South Africa', 'Mabibi', 'Explorer', 7, 'Liveaboard'],
    ['IND1', 'India', 'Mumbai', 'Blue Water', 7, 'Liveaboard'],
    ['IND2', 'India', 'Lakshadweep', 'Blue Water', 10, 'day boat'],
    ['OM1', 'Oman', 'Salalah', 'Explorer', 7, 'day boat'],
    ['OM2', 'Oman', 'Muscat', 'Blue Water', 7, 'Liveaboard']
    ]

for row in data:
    cursor.execute("insert into destinations values ('%s', '%s', '%s', '%s', %s, '%s');"%tuple(row))

connection.commit()

#Display records sorted by country
print("records sorted by country")
cursor.execute("select * from destinations order by country;")
for row in cursor.fetchall():
    print(row)

print()

#Q3: specific fields and records
print("Specifically selected columns and records")
command = "select `Holiday ID`, Region, Country from destinations"
command += " where `Liveaboard or day boat`='Liveaboard' AND `Number of days`=7 AND `Dive Boat Company`='Blue Water'"
command += " ORDER BY `Holiday ID`;"
cursor.execute(command)
for row in cursor.fetchall():
    print(row)

connection.close()
