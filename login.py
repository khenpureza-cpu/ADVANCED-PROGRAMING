# Act 10: Simple Login System 
correct_username = "khen"
correct_password = "khen1024"

while True:
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        print("Wrong username or password. Try again.")
