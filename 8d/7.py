from functools import reduce

kirish = ["salom", "dunyo", "nima", "gap"]

print(reduce(lambda x,y: x + " " + y, kirish))