from functools import reduce

lst = ["web", "development", "with", "python"]
n = list(map(lambda x: x.title() ,lst))
print(reduce(lambda x, y: x + " " + y, n)) 

####################################################

def check_anagram(word1: str, word2: str) -> bool:
    return sorted(word1.lower()) == sorted(word2.lower())

print(check_anagram("rAt","tar"))