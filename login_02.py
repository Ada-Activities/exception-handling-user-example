def login_02():
    
    user_data = {
        "name": "Crow T. Robot",
        "id": 11067
    }
    
    try:
        if user_data["is_logged_in"]:
            print(f"{user_data['name']}, "
                "you've successfully logged in!")
        else:
            print("You must log in to continue.")
            
    except KeyError as err :
        print("You've entered a key that "
            f"doesn't exist in 'user_data': {err}")

login_02()