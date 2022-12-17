"""
imports
"""
from collections import Counter
import string
from constants import FREQ_ENG, FREQ_PORT

"""
TODO:   acho que posso tranformar o get-groups e o get_columns em uma unica funcao get_mod_key_length
        so preciso do grupos separado de acordo com n (n = text_index % key_length)
"""


"""
divide o texto em grupos de tamanho group_size
"""
# TODO: ESTOU PEGANDO OS ' ' ESPACOS EM BRANCO, TEM QUE TIRAR
def Get_groups(text, group_size):
    # retira caracteres nao alfabeticos do texto
    new_text = ''

    for i in range(len(text)):
        if text[i].isalpha():
            new_text += text[i]

    #print(f'new text = {new_text}')

    groups = []
    
    for i in range(0, len(new_text), group_size):
        if (i + group_size) > len(new_text):
            dif = (i + group_size) - (len(new_text))
            g = new_text[i : len(new_text)]
            
            # completa o ultimo grupo com espacoes vazios
            for j in range(dif):
                g += ' '
            
            groups.append(g)
        else:
            groups.append(new_text[i : i + group_size])
    
    return groups

"""
 a coluna c de cada grupo
"""
def Get_columns(groups):
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

"""
conta quantas vezes cada letra apareceu no texto
"""
def Get_letter_count(column):
    uniform_column = column.lower()
    letter_count = Counter()

    for index, letter in enumerate(string.ascii_lowercase):
        letter_count[letter] = uniform_column.count(letter)

    return letter_count

"""
conta quantas vezes cada letra deveria aparecer no texto seguindo a distribuicao de frequencia normal da lingua inglesa
"""
def Get_exp_letter_count(text_len, mode):
    letter_count = Counter()

    if mode == 'english':
        for index, letter in enumerate(string.ascii_lowercase):
            letter_count[letter] = text_len * FREQ_ENG[letter]
    else:
        for index, letter in enumerate(string.ascii_lowercase):
            letter_count[letter] = text_len * FREQ_PORT[letter]

    return letter_count

"""
conta quantas vezes cada letra deveria aparecer no texto seguindo a distribuicao de frequencia normal da lingua portuguesa
"""