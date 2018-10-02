import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def giveMeaning(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        get = input("Did you mean %s? If Yes press y and if No press n" % get_close_matches(word, data.keys())[0])
        if get == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif get == 'n':
            return "The word doesn't exist. Please check it."
        else:
            return "Wrong input."

    else:
        return "The word doesn't exist. Please check it."


word = input("Enter a word: ")

output = giveMeaning(word)

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
