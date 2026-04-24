import os
import random
import string

# Define the length of the random string
length = 10

# Generate a string of random bytes and use them directly for each iteration
string_list = []
for i in range(10):
    # Use secure random bytes instead of character-based selection
    random_bytes = os.urandom(length)
    # Convert to hex string representation (secure)
    random_string = ''.join([format(random_bytes[n