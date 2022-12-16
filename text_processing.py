from collections import Counter
import string
from constants import EN_REL_FREQ

def get_groups(text, group_size):
    groups = []
    
    for i in range(0, len(text), group_size):
        if (i + group_size) > len(text):
            dif = (i + group_size) - (len(text))
            g = text[i : len(text)]
            
            for j in range(dif):
                g += ' '
            
            groups.append(g)
        else:
            groups.append(text[i : i + group_size])
    
    return groups


def get_columns(groups):
    group_size = len(groups[0])
    columns = []

    #print(f'g size = {group_size}')

    for l in range(group_size):
        c = ''
        for g in range(len(groups)):
            #print(f'g[{g}][{l}] = {groups[g][l]}')
            c += groups[g][l]
        columns.append(c)
    
    return columns


        #    for index, letter in enumerate(string.ascii_uppercase):
        #letter_counts[letter] = text_upper.count(letter)

def get_letter_count(column):
    uniform_column = column.lower()
    letter_count = Counter()

    for index, letter in enumerate(string.ascii_lowercase):
        letter_count[letter] = uniform_column.count(letter)

    return letter_count

def get_exp_letter_count(text_len):
    letter_count = Counter()

    for index, letter in enumerate(string.ascii_lowercase):
        letter_count[letter] = text_len*EN_REL_FREQ[letter]

    return letter_count
