import text_processing as tp
import string
from sys import maxsize
import constants as ct
from collections import Counter

"""
faz a cifracao ou decifracao dependendo so modo (mode) escolhido
"""

def cipher_decypher_aux(message_char, key_char, mode):
    if message_char.isalpha():

        # posicao da primeira letra e usada como referencial para descobrir o caracter cifrada 
        if message_char.islower():
            m_first_letter = ord('a')
        else:
            m_first_letter = ord('A')
        
        if key_char.islower():
            k_first_letter = ord('a')
        else:
            k_first_letter = ord('A')

        message_char_pos = ord(message_char) - m_first_letter
        key_char_pos = ord(key_char) - k_first_letter

        # posicao no alfabeto do novo caracter para cifracao ou decifracao
        if mode == 'cipher':
            new_message_char_pos = (message_char_pos + key_char_pos) % ct.ALPHABET_LEN
        else:
            new_message_char_pos = (message_char_pos - key_char_pos + ct.ALPHABET_LEN) % ct.ALPHABET_LEN
    else:
        # nao cifra caracteres nao alfabeticos, nao avanca nos caracteres da chave
        return (message_char,0)

    # retorna o caracter relativo a nova posicao
    new_message_char = chr(new_message_char_pos + m_first_letter)

    # avanca nos acaracteres da chave
    return (new_message_char,1)


"""
gerencia a funcao de cifracao e decifracao (cipher_decipher_aux)
"""

def cipher_decypher(text, key, mode):
    new_text = ''
    i = 0
    
    for text_char in text:
        # loop dos caracteres sa chave
        key_char = key[i%len(key)]
        text_code = cipher_decypher_aux(text_char, key_char, mode)
        # primeira parte da tupla tem o caracter
        new_text += text_code[0]
        # segunda parte da tupla tem o codigo que indica se e preciso ou nao avancar nos caracteres da chave
        i += text_code[1]

    return new_text


"""
def keyword_lenght(cyphertext):
    coincidence = list()

    for i in range(len(cipher_text)):
        i += 1
        count = 0

        for j in range(len(cipher_text) - i):
            if cipher_text[j] == cipher_text[j + i]:
                count += 1

        coincidence.append(count)

    #print(f'coincidence = {coincidence}')

    # distribuicao normal
    normalized_coincidence = [float(i)/max(coincidence) for i in coincidence]

    #print(f'normalized coincidence = {normalized_coincidence}')

    # index dos maiores valores de acordo com a distribuicao normal
    largest_20_percent = list()

    for i in range(len(normalized_coincidence)):
        if normalized_coincidence[i] > 0.8: # > 0.5, > 0.75, > 0.8 ???
            largest_20_percent.append(i)

    print(f'largest_20_percent = {largest_20_percent}')

    return largest_20_percent
"""


"""
verifica a ocorrencia dos fatores de divisao
"""
def factors(distances):
    factors_occurrences = []

    for f in range(3, ct.N_FACTOR):   # fatores de 3 a um numero definido
        count = 0
        for d in distances:
            if d%f == 0:    # verificamos se a distancia d e divisivel pelo fator f
                count += 1
        factors_occurrences.append((f, count))  # lista dos fatores e a quantidade de distanceias que eles dividem

    return factors_occurrences


def tuples(cyphertext):
    distance = []
    #list_strings = []
    i = 0
    
    while(i <= (len(cyphertext) - 3)): # < ou <=?
        flag_jumo_i = 0
        lenght_tuple = 3    # tamanho da tupla comeca com 3 e pode aumentar
        possible_tuple = cyphertext[i:i+lenght_tuple]

        for j in range((i+1), len(cyphertext)):
            if possible_tuple == cyphertext[j:j+lenght_tuple]: # se encontramos uma tupla repetida, aumentamos o tamamho da tupla
                #list_strings.append(possible_tuple)
                # acho que nao tem problema contabilizar duas vezes a mesma tupla
                flag_jumo_i = 1
                while (cyphertext[i:i+lenght_tuple] == cyphertext[j:j+lenght_tuple]) and (i+lenght_tuple < j): # precisa do 'if' ou pode ser so while
                    lenght_tuple += 1   # aumenta o tamano da tupla enquanto ambas forem iguais
                lenght_tuple -= 1   # se chegou aqui as tuplas passaram a ser diferentes, logo volta um passo no tamanho

                possible_tuple = cyphertext[i:i+lenght_tuple] # essa e a tupla. Precisa disso?

                # obter as distancias entre as ocorrencias das tuplas
                distance.append((j-i))
                
                j += lenght_tuple - 1

        if flag_jumo_i:
            i += lenght_tuple
        else:
            i += 1

    f = factors(distance)

    print(f'fatores = {f}')
    #print(f'distance = {distance}')


def get_chi_square(text, text_decyphered):
    text_len = len(text)
    expected_letters_count = tp.get_exp_letter_count(text_len)
    actual_letters_count = tp.get_letter_count(text_decyphered)

    #print(f'exp count = {expected_letters_count}')
    #print(f'act count = {actual_letters_count}')

    #error = Counter()
    #sq_error = Counter()
    normalized_error = Counter()

    for l in actual_letters_count:
        #error[l] = actual_letters_count[l] - expected_letters_count[l]
        #sq_error[l] = (error[l])^2
        normalized_error[l] = pow( (actual_letters_count[l] - expected_letters_count[l]), 2 ) / expected_letters_count[l]

    chi_square = sum(normalized_error.values())

    #print(f'norm err = {normalized_error}')
    #print(f'chi sq = {chi_square}')

    return chi_square


def get_key_letter(column):

    #print(f'columns = {columns}')

    chi_square = Counter()

    # decrifrar usando as letras do alfabeto (a - z)
    for index, letter in enumerate(string.ascii_lowercase):
        # coluna decifrada com a letra "letter"
        column_decyphered = cipher_decypher(column, letter, 'decypher')
        # lista com todos ao chi_square para todas as letras (a - z)
        chi_square[letter] = get_chi_square(column, column_decyphered)

    # a letra correspondente ao menor chi square

    print(f'chi square = {chi_square}')
    #sorted(x, key=x.get, reverse=True)
    print(f'chi square sorted = {sorted(chi_square, key=chi_square.get, reverse=False)}')
    key_letter = sorted(chi_square, key=chi_square.get, reverse=False)[0]

    print(f'key letter = {key_letter}')


    return key_letter

def get_key(cyphertext, key_length):
    groups = tp.get_groups(cyphertext, key_length)
    columns = tp.get_columns(groups)

    key = ''
    # para cada coluna
    for c in columns:
        key += get_key_letter(c)

    return key


def ic(letter_count, text_size):
    n = 0
    for l in letter_count:
        n += letter_count[l] * (letter_count[l] - 1)
    
    d = (text_size * (text_size-1))/ct.ALPHABET_LEN

    return n/d


def index_coincidence(cyphertext):
    groups = []
    columns = []
    minimum = maxsize
    key_length = 0

    for possible_key_length in range(2, ct.MAX_KEY_LENGTH):
        assumed_key_length = possible_key_length
        groups = tp.get_groups(cyphertext, assumed_key_length)
        #print(f'groups = {groups}')
        columns = tp.get_columns(groups)
        #print(f'columns = {columns}')

        index = 0

        for c in columns:
            letter_count = tp.get_letter_count(c)
            #print(f'letter count = {letter_count}')
            index += ic(letter_count, len(cyphertext))
            #print(f'ic = {ic(letter_count, len(cyphertext))}')

        avarege_index = index/assumed_key_length

        #print(f'avarege index = {avarege_index}')

        if (ct.IC_ENG - avarege_index) < minimum:
            minimum = ct.IC_ENG - avarege_index
            key_length = assumed_key_length
        
    return key_length


"""
descobrir o comprimento da palavra chave usando o metodo de Kasiski
"""

def keyword_lenght(cyphertext):
    #tuples(cyphertext)

    return index_coincidence(cyphertext)


"""
decifrar mensagem sem chave
"""

def decrypt(cyphertext):
    kl = keyword_lenght(cyphertext)

    key = get_key(cyphertext, kl)

    print(f'key length = {kl}')
    print(f'key  = {key}')

    cyphertext_decyphered = cipher_decypher(cyphertext, key, 'decypher')

    print(f'cyphertext decyphered: {cyphertext_decyphered}')



"""
programa principal
"""

"""
message = input('Insira mensagem que deseja cifrar: ')
key = input('Insira chave de cifracao (somente letras) ')

cipher_message = cipher_decipher(message, key, mode = 'cipher')
decipher_message = cipher_decipher(cipher_message, key, mode = 'decipher')

print(f'mensagem cifrada: {cipher_message}')
print(f'mensagem decifrada: {decipher_message}')
"""


cyphertext = input('Insira mensagem que deseja decifrar: ')

decrypt(cyphertext)