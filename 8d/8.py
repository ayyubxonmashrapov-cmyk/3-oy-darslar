from functools import reduce
st = ["olma", "banan", "anjir", "shaftoli"]

print(len(reduce(lambda y,x: y if len(y) > len(x) else x, st)))