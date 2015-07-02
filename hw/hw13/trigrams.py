from random import randint

# fileref = open("sherlock-small_txt.txt", "r")
fileref = open("sherlock.txt", "r")
text = fileref.readlines()
fileref.close


def remove_header(line_text):
    """Removes the any text that preceeds line_text, such as the eBook info"""
    scan = len(line_text)
    i = 0
    while (text[i][0:scan] != line_text):
        text[i] = " "
        i += 1
        # All lines leading up to line_text are cleared out


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
    """Generates a new sentence if a key cannot be found"""
    last_word = final[1]
    index = text.index(last_word)
    if (index != len(text) - 1):
        d.update({final: text[index + 1]})
        return
    else:
        d2 = d.copy()
        # We cannot iterate the original dictionary, since we're modifying it
        for tupal in d2:
            # Dictionaries are already random
            if (tupal[0][:1].isupper() and tupal[0] != "I"):
                # We are looking for a valid start of sentence
                d.update({final: [tupal[0]]})
                d.update({(final[1], tupal[0]): [tupal[1]]})
                # Two new keys must be created to link into the next
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
        # The output list is constantly being added too
    return(" ".join(output))


generate_keys()
print(output_story(500))
