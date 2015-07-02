from random import randint

fileref = open("sherlock-small_txt.txt", "r")
text = fileref.readlines()
d = {}
fileref.close

length = 500

text = " ".join(text)
text = text.split()
final = [text[0], text[1]]
final_text = text[0] + " " + text[1]


for word in range(len(text) - 2):
    key = (text[word], text[word + 1])
    third = text[word + 2]
    if (key not in d):
        d.update({key: [third]})
    else:
        d[key].append(third)

for i in range(length):
    key = (final[i], final[i + 1])
    next_invalid = True
    while (next_invalid):
        choices = d[key]
        third = choices[randint(0, len(choices) - 1)]
        next_key = (final[i + 1], third)
        next_invalid = (next_key not in d)
    final.append(third)
    final_text = final_text + " " + third

print(final_text)
