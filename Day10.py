user = {
    "admin":"1234",
    "user":"pass"
}

username = input("Username:")
password = input("Password:")

if username in user and user[username] == password:
    print("Login successful:")
else:
    print("Invalid Credentials")