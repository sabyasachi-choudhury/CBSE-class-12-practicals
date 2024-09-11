"""Assuming credit cards are stored as ints"""

import pickle

with open("transaction.dat", "rb") as file:
    while True:
        try:
            data = pickle.load(file)
            num = str(data[2])
            
            valid = True

            if num[0] != 4:
                valid = False
            if len(num) not in [13, 16]:
                valid = False
            if sum([2*int(char) for char in num[-2::-2]])%10 != 0:
                valid = False
                
            print(data[4], '/'.join(data[5].split(" ")), ':'.join(data[3].split(" ")), "$"+str(data[-1]), data[2], data[0], end=" ")
            if valid:
                print("Valid")
            else:
                print("Invalid")
        except:
            break
