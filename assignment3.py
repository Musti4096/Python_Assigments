number = input("Please enter any number: ")
while not number.isdigit():
    print("It is an invalid entry. Don't use non-numeric, float or negative values!")
    number = input("Please enter any number: ")
#print(len(number))
#print(word)
num = int(number)
toplam = 0
for i in range(len(number)):
    toplam += (int(number[i]) ** len(number))
if toplam == num:
    print(f"{number} is an Amstrong number!")
else:
    print(f"{number} is not an Amstrong number")
