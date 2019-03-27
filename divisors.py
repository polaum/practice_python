x = range(2, 11)
divisors = []
num = int(input("Choose a number to check: "))
for i in x:
    if num % i == 0:
        divisors.append(int(num/i))

print(divisors)
