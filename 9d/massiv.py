def juftlar_soni(lst:list ) -> int:
    y=0
    for i in lst:
        if i % 2 == 0:
            y += 1
    return y

def toqlar_chiqar(lst:list):
    for i in lst:
        if i % 2 != 0:
            print(i)        

def max_top(lst:list) ->int:
   return max(lst)
