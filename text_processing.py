from collections import Counter as c

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

    print(f'g size = {group_size}')

    for l in range(group_size):
        c = ''
        for g in range(len(groups)):
            print(f'g[{g}][{l}] = {groups[g][l]}')
            c += groups[g][l]
        columns.append(c)
    
    return columns

def get_letter_count(column):
    uniform_column = column.lower()
    letter_count = c()

    for letter in uniform_column:
        letter_count[letter] += 1

    return letter_count
