n = [int(input("Enter a year in four digit: "))]

a = list(map(lambda x: "is a Leap year" if x%4 == 0 or ( x % 100 != 0 or x % 400 == 0) else "is not a Leap year" , n))

print(f"{n[0]} {a[0]}")
