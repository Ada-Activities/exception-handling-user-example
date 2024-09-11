def login_01():
    
    user_data = {
        "name": "Crow T. Robot",
        "id": 11067
    }
    
    if user_data["is_logged_in"]:
        print(f"{user_data['name']}, "
            "you've successfully logged in!")
    else:
        print("You must log in to continue.")

login_01()