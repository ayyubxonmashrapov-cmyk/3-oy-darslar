products = [
    ("apple", 1.2),
    ("banana", 0.8),
    ("milk", 2.5),
    ("bread", 1.5),
    ("tea", 2.5)
]

for i in range(len(products)-1):
    for j in range(i+1,len(products)):
        if products[i][1] > products[j][1]:
            products[i],products[j] = products[j],products[i]

a = products[-1][1]

for i in range(len(products)-1, -1, -1):
    if products[i][1] != a:
        print(products[i])
        break
    


