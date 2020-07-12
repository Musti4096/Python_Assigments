number = int(input("Please enter a number"))


if (number % 1 == 0) and (number % number == 0 ) and (number % 2 != 0) and (number % 3 != 0) and (number % 5 != 0) and (number % 7 != 0):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
