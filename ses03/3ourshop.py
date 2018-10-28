items = ["T-Shirt","Sweater"]
chose = input("Welcom to our shop, what do you want (C, R, U, D) ? ")

if chose == "R":
    print("Our items: ",*items,sep=",")
    chose = input("Welcom to our shop, what do you want (C, R, U, D) ? ")

if chose == "C":
    new = input("Enter new item: ")
    items.append(new)
    print("Our items: ",*items,sep=",")
    chose = input("Welcom to our shop, what do you want (C, R, U, D) ? ")

if chose =="U":
    i = int(input("Update position? "))
    new = input("New item ? ")
    items[i-1] = new
    print("Our items: ",*items,sep=",")
    chose = input("Welcom to our shop, what do you want (C, R, U, D) ? ")
if chose =="D":
    i = int(input("Delete position? "))
    print("Our items: ",*items,sep=",")
    chose = input("Welcom to our shop, what do you want (C, R, U, D) ? ")
