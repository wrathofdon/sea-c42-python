from random import randint

# fileref = open("sherlock-small_txt.txt", "r")
fileref = open("sherlock.txt", "r")
text = fileref.readlines()
fileref.close


def remove_header(line_text):
    scan = len(line_text)
    i = 0
    while (text[i][0:scan] != line_text):
        text[i] = " "
        i += 1


remove_header("To Sherlock Holmes she")


d = {}
# create empty dictionary for trigrams
text = " ".join(text)
text = text.split()
# convert text to string, the split it into list of individual words
output = [text[0], text[1]]
# output starts with first two words as novel.



def generate_keys():
    for word in range(len(text) - 2):
        key = (text[word], text[word + 1])
        third = text[word + 2]
        # each trigram combines three words
        if (key not in d):
            d.update({key: [third]})
        else:
            d[key].append(third)
        # We add the word paid to the dictionary if it's not already there.


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


def output_story(length):
    for i in range(length):
        key = (output[i], output[i + 1])
        if (key not in d):
            final_key(key)
            # Key will be automatically generated if it isn't already available
        choices = d[key]
        third = choices[randint(0, len(choices) - 1)]
        output.append(third)
    return(" ".join(output))


generate_keys()
print(output_story(500))
