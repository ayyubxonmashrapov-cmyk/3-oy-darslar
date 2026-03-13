son = 1020003
yoq0 = 0
daraja = 1
while son:
    if son % 10:
        yoq0 += (son % 10)  * daraja
        daraja *= 10
    son //= 10 
print(yoq0)
