from PyInquirer import prompt
import csv

def new_expense(*args):

    with open('users.csv', newline='') as u:
        reader = csv.reader(u)
        users = list(reader)

    print(users)
    infos = prompt([
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        'choices': [{'name': x[0], } for x in users],
    },])
    thespender = infos["spender"]
    who = prompt([
    {
        "type":"checkbox",
        "name":"for",
        "message":"New Expense - paid for: ",
        'choices': [{'name': x[0], 'checked': (True if x[0] == thespender else False)} for x in users],
    },
])
    f = open("expenses.csv", "a")
    f.write(infos["amount"] + ',' + infos["label"] + "," + infos["spender"] + "," + str(who["for"]) + "\n")
    f.close()

    value = int(infos["amount"]) /(1 + len(who))
    print(value)

    with open('users.csv', newline='') as u:
        reader = csv.reader(u)
        allusers = list(reader)

    for k in allusers:
        if (k[0] in who["for"]):
            print("HIM! + ", k[0])
            if (k[0] != thespender):
                k[1] = str(int(k[1]) + int(value))
            if (k[0] == thespender):
                k[2] = str(int(k[2]) + int(infos["amount"]) - int(value))
    
    print(allusers)

    open('users.csv', 'w').close()

    with open('users.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for line in allusers:
            writer.writerow(line)
    


    print("Expense Added !")
    return True


