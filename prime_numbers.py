n = int(input("Enter a limit number"))

prime_numbers = []

for num in range(2, n+1):
    status = True
    for i in range(2, num):
        if num % i == 0:
            status = False
    if status:
        prime_numbers.append(num)
    
print(prime_numbers)
