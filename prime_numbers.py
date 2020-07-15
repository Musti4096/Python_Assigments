n = int(input("Enter a limit number"))
prime_numbers = [2]
for i in range(2, n+1):
    for j in range(2, i+2):
        if i%j == 0:
            break
        elif j+1 == i :
            prime_numbers.append(i)
        else: pass
print(prime_numbers)
