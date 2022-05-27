# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

import string


def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename,'r') as f:
        file = f.read().replace('\n', '')
    
    return file


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    d = dict()

    for character in string.punctuation:
        text = text.replace(character, "").lower()
    chats = text.split()

    for word in chats:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1

    for key in list(d.keys()):
        print(key, ":", d[key])

count_words()