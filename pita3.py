import random

# Generate 399 random numbers between 1 and 399
random_numbers = [random.randint(0, 399) for _ in range(399)]

# Save the random numbers to a text file
with open('random_numbers.txt', 'w') as file:
    for number in random_numbers:
        file.write(str(number)+'\n')