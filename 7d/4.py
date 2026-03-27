from random import randint
def n_tasodifiy_son(n:int)->int:
    return randint(10**(n-1),10**n - 1)


print(n_tasodifiy_son(int(input())))

