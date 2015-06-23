import random

alphabet = "abcdefghijklmnopqrstuvwxyz "

alphabet_list = list(alphabet)

# Create a new copy of alphabet list
cipher_list = list(alphabet_list)

# This should be a list in order
print(cipher_list)

message_text = "what has dates and sundays but cannot be eaten"

random.shuffle(cipher_list)

# This should be random now
print(cipher_list)

cipher_text = ""

for x in message_text:
    index = alphabet_list.index(x)
    cipher_char = cipher_list[index]
    cipher_text += cipher_char

# This is what
print(cipher_text)
