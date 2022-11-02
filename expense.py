from PyInquirer import prompt
import csv

users = []

with open('users.csv', newline='') as u:
    reader = csv.reader(u)
    users = list(reader)

expense_questions = [
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
    },
]





def new_expense(*args):
    infos = prompt(expense_questions)
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
    f.write(infos["amount"] + ';' + infos["label"] + ";" + infos["spender"] + ";" + str(who["for"]) + "\n")
    f.close()
    print("Expense Added !")
    return True


