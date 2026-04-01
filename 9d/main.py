from massiv import *

sonlar = input("prober bilan snlar kiriting: ").split()
sonlar = list(map(int,sonlar))
 

while True:
    print("\n=== Asosiy menyu ===")
    print("1. Toqlarni chiqarish")
    print("2. Juftlar soni")
    print("3. Maksimal qiymat")
    print("4. Chiqish")

    tanlov = input("Tanlovingizni kiriting: ")

    if tanlov == "1":
        toqlar_chiqar(sonlar)
        
    elif tanlov == "2":
        print(juftlar_soni(sonlar))
        
    elif tanlov == "3":
        print(max_top(sonlar))
        
    else:
        break


