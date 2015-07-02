from random import randint

fileref = open("sherlock-small_txt.txt", "r")
text = fileref.readlines()
fileref.close
d = {}


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


def final_key(final):
    last_word = final[1]
    index = text.index(last_word)
    if (index != len(text) - 1):
        d.update({final: text[index + 1]})
        return
    else:
        d2 = d.copy()
        for tupal in d2:
            if (tupal[0][:1].isupper() and tupal[0] != "I"):
                d.update({final: [tupal[0]]})
                d.update({(final[1], tupal[0]): [tupal[1]]})
                print("final: ", final, tupal[0], tupal[1])
                print("final2: ", d[final])
                return
            else:
                pass


final = (text[-2], text[-1])
if (final not in d):
    final_key(final)

for i in range(length):
    key = (output[i], output[i + 1])
    choices = d[key]
    third = choices[randint(0, len(choices) - 1)]
    output.append(third)

print(" ".join(output))
