def alohida_son(n:int)->int:
    if n == 0:
        return 
    print(n%10, end=" ")
    
    alohida_son(n //10)


alohida_son(int(input()))