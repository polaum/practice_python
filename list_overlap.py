a = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89}
b = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}

print(list(a.intersection(b)))


c = list(dict.fromkeys(filter(lambda x: x in b, a)))
print(c)

d = list(set(filter(lambda x: x in b, a)))
print(d)
