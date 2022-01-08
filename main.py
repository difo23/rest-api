

def load_data():
    try:
        json_url = os.path.join("data", "data.json")
        data_json = json.load(open(json_url))
        return data_json
    except:
        print("An exception occurred")
        return None


def load_users_names():
    try:
        json_url = os.path.join("data", "data.json")
        data_json = json.load(open(json_url))
        users = data_json["users"]
        names = [x["name"] for x in users]
        return names
    except:
        print("An exception occurred")
        return None


def add_user(name):
    try:
        json_url = os.path.join("data", "data.json")
        user = {
            "name": name,
            "owes": {},
            "owed_by": {},
            "balance": 0
        }
        with open(json_url, "r+") as file:
            data_json = json.load(file)
            data_json["users"].append(user)
            file.seek(0)
            json.dump(data_json, file)
        return user
    except:
        print("An exception occurred")
        return None


def update_users(lender, borrower):
    try:
        json_url = os.path.join("data", "data.json")
      

        with open(json_url, "r+") as file:
            data_json = json.load(file)
            users = data_json["users"]

            for i in range(len(users)):
                name = users[i]["name"]
                if lender["name"] == name:
                    users[i] = lender
                if borrower["name"] == name:
                    users[i] = borrower
        with open(json_url, "w") as file:
            json.dump(data_json, file)

        return {"users": [lender, borrower]}
    except:
        print("An exception occurred")
        return None


def filter_user(names_query):
    users = []
    for name in names_query:
        user = get_user(name)
        if user:
            users.append(user)
    return users

# Not efficient


def get_user(username):
    data_json = load_data()
    users = data_json["users"]
    for user in users:
        if username == user["name"]:
            return user
    return False


def exists(name):
    names = load_users_names()
    return True if name in names else False


def update_IOU(lender, borrower, amount):

    lender_name = lender["name"]
    lender_owed_by = lender["owed_by"]
    lender_balance = int(lender["balance"])

    borrower_name = borrower["name"]
    borrower_owes = borrower["owes"]
    borrower_balance = borrower["balance"]

    # "balance": "<(total owed by other users) - (total owed to other users)>"

    # Adam {'Bob': 6.5, 'Dan': 2.75} -16
    # Bod {'Adam': 6.5, 'Chuck': 3.0} -8.5

    lender_owed_by = update_dic(borrower_name, lender_owed_by, amount)
    borrower_owes = update_dic(lender_name, borrower_owes, amount)

    borrower_balance -= amount
    lender_balance += amount

    lender["balance"] = lender_balance
    borrower["balance"] = borrower_balance

    print(lender)
    print(borrower)

    return update_users(lender, borrower)


def update_dic(name, dic, value):
    if name in dic.keys():
        dic[name] += value
    else:
        dic[name] = value
    return dic
