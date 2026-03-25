# n = int(input("n(n>0)kiriting: "))
n = 10
ls = [0,1]
i = 2
while ls[i-1]+ls[i-2] < n:    
    ls.append(ls[i-1]+ls[i-2])
    i+=1
print(ls)

