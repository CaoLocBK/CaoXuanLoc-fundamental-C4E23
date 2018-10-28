superuser = "c4e"
pwd = "codethechange"

print("Hi there, this is a superuser gateway")
us1 = input("Username: ")
while True :
    if us1 != superuser:
        print("You are not superuser")
        us1 = input("Username: ")
    else:
        break
pd = input("Password: ")
while True:
    if pd != pwd:
        print("Password is incorrect")
        pd = input("Password: ")
    else:
        break
print("Welcome, c4e")