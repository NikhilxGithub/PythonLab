import random

# Generate a set containing 10 randomly generated numbers in the range 15 to 45
random_numbers = set(random.randint(15, 45) for _ in range(10))

print("Generated numbers:", random_numbers)

# Count how many generated numbers are less than 30
count_less_than_30 = sum(1 for num in random_numbers if num < 30)
print("Count of numbers less than 30:", count_less_than_30)

# Delete all numbers greater than 35
random_numbers = {num for num in random_numbers if num <= 35}

print("After deleting numbers greater than 35:", random_numbers)