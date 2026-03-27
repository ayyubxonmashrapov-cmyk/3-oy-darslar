lst = [(2, 5, "1210"), (1, 2, "210"), (4, 4, "150"), (2, 3, "640"), (2, 1, "710")]

# for j in range(len(lst)-1):
#     for i in range(len(lst)-1):
#         if lst[i][1] > lst[i+1][1]:
#             lst[i], lst[i+1] = lst[i+1], lst[i]


lst.sort(key=lambda value: int((value[2])))
print(lst)