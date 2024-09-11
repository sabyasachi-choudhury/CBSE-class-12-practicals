import csv

def decrypt():
    f2 = open("decrypt.csv", "w", newline='')
    writer = csv.writer(f2)
    to_write = [['Encrypted',
                'Date Digits',
                'Date of Transaction',
                'Bank Sort Code',
                'Account Number',
                'Transmitted Check Digit',
                'Calculated Check Digit',
                'Working 1',
                'Transaction',
                'Working 2',
                'Credit',
                'Debit']]

    with open('encryptTransactions.csv', "r") as file:
        for [x] in csv.reader(file):
            check_digit = x[0]
            bank_sort_code = f"{x[1]}{x[2]}-{x[3]}{x[4]}-{x[5]}{x[6]}"
            account_number = x[7:16]
            date_digits = x[16:24]
            date = f"{x[16]}{x[17]}/{x[18]}{x[19]}/{x[20:24]}"
            transaction = x[24]
            working_2 = x[25:]
            check_sum = sum([int(c) for c in account_number])%10
            if check_sum == check_digit:
                working_1 = 'checks match'
            else:
                working_1 = 'checks failed'
            if transaction == 'C':
                credit = int(working_2)/100
                debit = 0
            else:
                debit = int(working_2)/100
                credit = 0

            to_write.append([x, date_digits, date, bank_sort_code, account_number, check_digit, check_sum, working_1, transaction, working_2, credit, debit])

    writer.writerows(to_write)
    f2.close()

def display():
    reader = csv.reader(open("decrypt.csv", "r"))
    for elem in reader:
        print(elem)

decrypt()
display()
