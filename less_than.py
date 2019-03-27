a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 4]


num = int(input("Choose a number to check: "))
less_than = list(filter(lambda x: x < num, a))
print(less_than)
