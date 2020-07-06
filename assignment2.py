age = input("Are you a cigarette addict older than 75 years old? (Yes or No): ").title()
chronic = input("Do you have a severe chronic disease? (Yes or No)").title()
immune = input("Is your immune system too weak? (Yes or No)").title()

if (age == "Yes") and (chronic == "Yes") and (immune == "Yes"):
    print("You are in risky group")
else:
    print("You are not in risky group")
