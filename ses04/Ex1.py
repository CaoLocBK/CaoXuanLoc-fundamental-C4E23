flo = [5, 7, 8, 300, 90, 24, 50, 75]
#2.1
print("Hello, my name is Loc and these are my ship sizes")
print(flo)
ma = flo[0]
#2.2
for i in flo:
    if i > ma:
        ma = i
print("Now my biggest sheep has size", ma ,"let's shear it")

#2.3
flo.remove(ma)
print("After shearing, here is my flock",flo,sep = '\n')

#2.4
print("One month has passed, now here is my flock")
x = len(flo)
print(x)
print(type(x))
for i in range(x):
    flo[i]+=50
print(flo)
for i in flo:
    if i > ma:
        ma = i

#2.5
for i in range(3):
        print("Month: ",i+1)
        print("Hello, my name is Loc and here is my flock",flo)
        for t in range(x):
                flo[t]+=50
                print(flo)
        mb = flo[0]
        for i1 in flo:
                if i1 > mb:
                        mb = i1
        flo.remove(mb)

