import pickle

data = []
with open("library.dat", "rb") as file:
    while True:
        try:
            data.append(pickle.load(file))
        except EOFError:
            break

key = lambda x: x[-1]
data.sort(key = key)

# Total and Average Books
s = sum([k[-1] for k in data])
print(f"Total Books Read: {s}\nAverage Books Read: {s/len(data)}")

# less than 10 books
print("\nThe following students have read less than 10 books")
for student in data:
    if student[-1] < 10:
        print(student[0])
    else:
        break

# Top 3
print("\nGold Medallist")
print(f"ID: {data[-1][0]} | Name: {data[-1][1]} {data[-1][2]} | Books Read: {data[-1][3]}\n")
print("Silver Medallist")
print(f"ID: {data[-2][0]} | Name: {data[-2][1]} {data[-2][2]} | Books Read: {data[-2][3]}\n")
print("Bronze Medallist")
print(f"ID: {data[-3][0]} | Name: {data[-3][1]} {data[-3][2]} | Books Read: {data[-3][3]}\n")
