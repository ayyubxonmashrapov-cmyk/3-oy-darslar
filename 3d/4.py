harf = "sadf"
while len(harf) != 1:
    print("Bitta harf kiriting")
    harf = input("Harf kiriting: ").lower()



if harf in "euioa":
    print("Unli")
elif harf in "qwrtypsdfghjklzxcvbnm":
    print("Undosh")
else:
    print("belgi")    