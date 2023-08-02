# How will you set the starting value in generating random numbers?

import random

# Set the seed value
random.seed(13)

# Generate random numbers same for seed value 13
random_number = random.randint(1,100)
print(random_number)