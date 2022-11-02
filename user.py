from PyInquirer import prompt
import csv
user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New user - name: ",
    },
    {
        "type":"input",
        "name":"debt",
        "message":"New user - debt: ",
    },
    {
        "type":"input",
        "name":"owed",
        "message":"New user - how much people owe him: ",
    },
]

def add_user():
    infos = prompt(user_questions)
    f = open("users.csv", "a")
    f.write(infos["name"] + "," + infos["debt"] + "," + infos["owed"] + '\n')
    f.close()
    print("User Added !")
    return True

def summary():
    with open('users.csv', newline='') as u:
        reader = csv.reader(u)
        users = list(reader)
    
    for line in users:
        print("user " + line[0] + " owes " + line[1])