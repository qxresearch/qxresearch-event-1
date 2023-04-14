import secrets

# rand_bytes = secrets.token_bytes(4)
# print("Random bytes:", rand_bytes)

number_list = []
for i in range(10):
    number_list.append(secrets.randbelow(10000) + 1)

print(number_list)