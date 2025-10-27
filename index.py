# import requests as r
# def registerdata():
#     username=input("enter username: ")
#     password=input("enter password: ")
#     email=input("enter email: ")

#     if len(username)==0 or len(password)==0 or len(email)==0:
#         print("enter the details properly")
#         return registerdata()
#     else:
#         dicct= {
#             "user":username,
#             "pass":password,
#             "email":email
#     }
#     return dicct  
     
# ress=r.get("http://localhost:3000/posts")
# data1=ress.json()
# data=registerdata()
# exists=False
# for i in data1:
#     if i["user"]==data["user"]:
#         exists=True
# if exists:
#     print("username already exists")
# else:
#     res=r.post("http://localhost:3000/posts",json=data)
#     print("user added successfully")
#     print(res.json())

# def logindata():
#     username = input("enter username to login: ")
#     password = input("enter password to login: ")
#     response = r.get("http://localhost:3000/posts")
#     data = response.json()
#     found = False
#     for user in data:
#         if user.get("user") == username and user.get("pass") == password:
#             found = True
#             break

#     if found:
#         print("Login successful! Welcome,", username)
#     else:
#         print("Login failed! Invalid username or password.")

# def main():
#     new_user = registerdata()
#     if new_user:
#         logindata()

# main()




import requests as r

def registerdata():
    username = input("enter username: ")
    password = input("enter password: ")
    email = input("enter email: ")

    if len(username) == 0 or len(password) == 0 or len(email) == 0:
        print("enter the details properly")
        return registerdata()
    else:
        dicct = {
            "user": username,
            "pass": password,
            "email": email
        }
        return dicct

def register_user():
    ress = r.get("http://localhost:3000/posts")
    data1 = ress.json()
    data = registerdata()
    exists = False

    for i in data1:
        if i["user"] == data["user"]:
            exists = True
            break

    if exists:
        print("username already exists")
        return None
    else:
        res = r.post("http://localhost:3000/posts", json=data)
        print("user added successfully")
        print(res.json())
        return data

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
    new_user = register_user()
    if new_user:
        logindata()

main()
