my_pass = {"Mustafa": "Pp123456", "Züleyha": "Aa123456"}
name = input("Please enter your name: ").title()
#name in my_pass
if name in my_pass:
    print(f"Hello, {name}! The password is:{my_pass[name]}")
else:
    print(f"Hello, {name}! See you later.")
