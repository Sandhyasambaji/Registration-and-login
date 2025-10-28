import requests as r
def registerdata():
    username=input("enter username: ")
    password=input("enter password: ")
    email=input("enter email: ")

    if len(username)==0 or len(password)==0 or len(email)==0:
        print("Please fill in all fields!")
        return registerdata()
    else:
        dicct= {
            "user":username,
            "pass":password,
            "email":email
    }
    
     
    ress=r.get("http://localhost:3000/posts")
    users=ress.json()

    exists=False
    for i in users:
        if i.get("user")==username:
            exists=True
            break
    if exists:
        print("username already exists")
    else:
        res=r.post("http://localhost:3000/posts",json=dicct)
        print("user registered successfully!")

def logindata():
    username = input("enter username to login: ")
    password = input("enter password to login: ")
    response = r.get("http://localhost:3000/posts")
    data = response.json()
    found = False
    for user in data:
        if user.get("user") == username and user.get("pass") == password:
            found = True
            break

    if found:
        print("Login successful! Welcome,", username)
    else:
        print("Login failed! Invalid username or password.")

def main():
    while True:
        print("\n=== MENU ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            registerdata()
        elif choice == "2":
            logindata()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()








