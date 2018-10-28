superuser = "c4e"
pwd = "codethechange"

print("Hi there, this is a superuser gateway")
us1 = input("Username: ")
if us1 != superuser:
        print("You are not superuser")
        us1 = input("Username: ")

pd = input("Password: ")
if pd != pwd:
        print("Password is incorrect")
        pd = input("Password: ")

print("Welcome, c4e")