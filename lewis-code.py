"""
Theme Park Ticket Machine
"""

# Ask for the visitor's information.
print("WELCOME TO THE THEME PARK!")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))
vip = input("Do you have a VIP pass? (YES or NO): ").strip().upper()

# Select the ticket price based on age.
# if/elif/else checks age ranges in order so each visitor gets one price.
if age < 5:
    price = 0.0
elif age <= 12:
    price = 15.0
else:
    price = 40.0

# A VIP pass gives a 20% discount, so the visitor pays 80% of the price.
if vip == "YES":
    price *= 0.8

# The visitor must be at least 12 AND at least 140 cm tall.
# Using 'and' means both conditions must be true.
if age >= 12 and height >= 140:
    allowed = True
else:
    allowed = False

# Show the final ticket price and roller coaster decision.
print()
print(f"Hello {name}!")
print(f"Ticket price: ${price:.2f}")

if allowed:
    print("Extreme Roller Coaster: ALLOWED")
else:
    print("Extreme Roller Coaster: NOT ALLOWED")

print("Enjoy your day!")