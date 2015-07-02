from random import randint

fileref = open("sherlock-small_txt.txt", "r")
text = fileref.readlines()
d = {}
fileref.close


text = " ".join(text)
text = text.split()
output = [text[0], text[1]]
length = 500

for word in range(len(text) - 2):
    key = (text[word], text[word + 1])
    third = text[word + 2]
    if (key not in d):
        d.update({key: [third]})
    else:
        d[key].append(third)


def final_key():
    final = (text[-2], text[-1])
    if (final in d):
        return
    else:
        d2 = d.copy()
        tupal = ("false", "false")
        for tupal in d2:
            if (tupal[0][:1].isupper()):
                print(tupal)
                d.update({final: tupal[0]})
                d.update({(text[-1], tupal[0]): tupal[1]})
        else:
            final_key()


final_key()

for i in range(length):
    key = (output[i], output[i + 1])
    choices = d[key]
    third = choices[randint(0, len(choices) - 1)]
    output.append(third)

print(" ".join(output))
