from datetime import date

current_year = date.today().year

birth_year = int(input("Enter your birth year: "))

age = current_year - birth_year

print(f"You are {age} years old.")