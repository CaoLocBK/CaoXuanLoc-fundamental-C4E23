prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock ={
"banana": 6,
"apple": 0,
"orange": 32,
"pear": 15
}
total = 0
print("Apple")
print("price:",prices["apple"])
print("stock",stock["apple"])

print("Pear")
print("Price:",prices["pear"])
print("stock:",stock["pear"])

for i in prices:
    print(i,prices[i],stock[i])
    total = prices[i]*stock[i]
print(total)


