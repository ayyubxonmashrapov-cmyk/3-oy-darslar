from random import randint


royxat = []
for i in range(20):
    son = randint(1,100)
    royxat.append(son)

print(royxat)
royxat.remove(max(royxat))
royxat.remove(min(royxat))

print(max(royxat))
print(min(royxat))