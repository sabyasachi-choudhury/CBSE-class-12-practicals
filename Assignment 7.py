with open("Sales.txt", "r") as file:
    total = 0
    for row in file.readlines():
        data = row[:-1].split(",")
        s = sum([int(x) for x in data[3:]])
        print(f"Employee {data[0]}: {data[1]} {data[2]} | net sales: {s} USD")
        total += s
    print(f"\nTotal sales by team: {total} USD")
