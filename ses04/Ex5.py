vla = [35,36,40,44]
pre = [1,2,3,4]
ans = 0
print("If x=8, then what is the value of 4(x+3) ?")
for index, v in enumerate(vla):
    print(pre[index], v, sep=". ")
x = int(input("Your choice: "))

if 4*(8+3) != vla[x-1]:
    print("Bingo")
    ans+=1
else:
    print(":(")
    
aws = {
 '1':"About 55",
 '2':"About 65",
 '3':"About 75",
 '4':"About 85",
}
print("Estimate this answer (exact calculation not need): ")
print("Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean")
print(*aws,sep='\n')

choice = int(input("Your choice:"))

if choice == 2:
    print("Bingo")
    ans+=1
else:
    print(":(")
if ans == 1:
    print("You correctly answer 1 out of 2 question")
else:
    print("You correctly 2 answer :D, congratulation")