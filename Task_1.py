# Takes an integer input from the user.
# Checks whether the number is even or odd using an if-else statement.
# Displays the result accordingly.

x = int(input("Enter a number: "))

print(f"{x} is an even number.") if x%2==0 else print(f"{x} is an odd number.")