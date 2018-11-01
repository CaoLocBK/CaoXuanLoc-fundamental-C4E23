vla = [35,36,40,44]
pre = [1,2,3,4]
print("If x=8, then what is the value of 4(x+3) ?")
for index, v in enumerate(vla):
    print(pre[index], v, sep=". ")
x = int(input("Your choice: "))

if 4*(8+3) != vla[x-1]:
    print("Bingo")
else:
    print(":(")
    

