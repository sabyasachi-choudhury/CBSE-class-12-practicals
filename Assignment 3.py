"""Assignment 3"""

def letter_count(string: str, counts: dict):
    for char in string:
            if char in counts.keys():
                counts[char] += 1
            else:
                counts[char] = 1

numcount = {}
s = input("enter string you want to count: ")
letter_count(s, numcount)
for (key, value) in numcount.items():
    print(f"{key} : {value}")
