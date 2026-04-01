
try:
    a, b = int(input("a=")), int(input("b="))
    try:
        print(a//b)
    except ZeroDivisionError:
        print("b 0ga teng bolmasin")    

except ValueError:
    print("faqat son")


    