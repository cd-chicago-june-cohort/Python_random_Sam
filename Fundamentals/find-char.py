def find_char(strings, char):
    newstrings = []
    for word in strings:
        letter = word.count(char)
        if letter > 0:
            newstrings.append(word)
    print newstrings

find_char(['hello','world','my','name','is','Anna'], 'o')
