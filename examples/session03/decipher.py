# This is the file for the deciphering partner.

alphabet = "abcdefghijklmnopqrstuvwxyz "

alphabet_list = list(alphabet)

# Copy and paste the cipher list from your partner below,
# instead of the empty list.
cipher_list = ['v', 'w', 'u', 'q', 'k', 'm', 'g', 'z', 'l', 'n', 'e', ' ', 'd', 'b', 'x', 'y', 'i', 't', 'f', 'h', 'r', 'c', 'j', 'a', 'p', 's', 'o']


# copy and paste the cipher_text from your partner in slack
# and assign it to the variable new_cipher_text
new_cipher_text = "jzvhozvfoqvhkfovbqofrbqvpfowrhouvbbxhowkokvhkb"

decrypt_text = ""

for y in new_cipher_text:
    index = cipher_list.index(y)
    decrypt_char = alphabet_list[index]
    decrypt_text += decrypt_char

print(decrypt_text)
