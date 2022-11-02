from PyInquirer import prompt
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
]

def add_user():
    infos = prompt(user_questions)
    f = open("users.csv", "a")
    f.write(infos["name"] + ";" + infos["debt"])
    f.close()
    print("User Added !")
    return True