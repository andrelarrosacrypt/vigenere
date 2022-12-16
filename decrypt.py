"""
imports
"""
from cipher_decipher import Cipher_decipher
from sys import maxsize
from constants import ALPHABET_LEN, IC_ENG, MAX_KEY_LENGTH
import text_processing as tp
from collections import Counter
import string

"""
calcula a distribuicao qui-quadrado para cada possivel decifracao
https://en.wikipedia.org/wiki/Chi-squared_distribution
"""
def Chi_square(text, possible_decyphered_text):
    text_len = len(text)
    expected_letters_count = tp.Get_exp_letter_count(text_len)
    actual_letters_count = tp.Get_letter_count(possible_decyphered_text)

    #print(f'exp count = {expected_letters_count}')
    #print(f'act count = {actual_letters_count}')

    normalized_error = Counter()

    for l in actual_letters_count:
        # error = actual_letters_count - expected_letters_count
        # sq_error = error^2
        normalized_error[l] = pow( (actual_letters_count[l] - expected_letters_count[l]), 2 ) / expected_letters_count[l]

    # soma de todos os erros quadraticos normalizados
    chi_square = sum(normalized_error.values())

    #print(f'norm err = {normalized_error}')
    #print(f'chi sq = {chi_square}')

    return chi_square

"""
descobre a letra que foi usada para cifrar o grupo
"""
def Key_letter(column):
    #print(f'columns = {columns}')
    chi_square = Counter()

    # verificar dentre as letras do alfabeto (a - z) qual a que cifrou esse grupo
    for index, letter in enumerate(string.ascii_lowercase):
        # coluna possivelmente decifrada
        possible_decyphered_column = Cipher_decipher(column, letter, 'decypher')
        # lista com todos ao chi_square para todas as letras (a - z)
        chi_square[letter] = Chi_square(column, possible_decyphered_column)

    #print(f'chi square = {chi_square}')
    #print(f'chi square sorted = {sorted(chi_square, key=chi_square.get, reverse=False)}')
    
    # menor distribuicao qui_quadrado e a letra que realmente cifra/decifra o grupo
    key_letter = sorted(chi_square, key=chi_square.get, reverse=False)[0]

    #print(f'key letter = {key_letter}')

    return key_letter

"""
controi a chave que decifra o texto
"""
def Key(ciphertext, key_length):
    groups = tp.Get_groups(ciphertext, key_length)
    columns = tp.Get_columns(groups)

    key = ''
    # para cada coluna
    for c in columns:
        key += Key_letter(c)

    return key

"""
calcula o indice de coincidencia do grupo
"""
def Index_coincidence(letter_count, text_size):
    numerator = 0
    # para cada letra pertencente ao grupo
    for l in letter_count:
        numerator += letter_count[l] * (letter_count[l] - 1)

    denominator = ( text_size * (text_size-1) )/ALPHABET_LEN
    
    index_coincidence = numerator/denominator

    return index_coincidence

    
"""
descobre o comprimento da palavra chave usando indice de coincidencia
"""
def Keyword_lenght(ciphertext):
    groups = []
    columns = []
    minimum = maxsize
    key_length = 0

    # para cada possivel comprimento de chave
    for possible_key_length in range(2, MAX_KEY_LENGTH):
        groups = tp.Get_groups(ciphertext, possible_key_length)
        #print(f'groups = {groups}')
        columns = tp.Get_columns(groups)
        #print(f'columns = {columns}')

        index = 0

        # para cada coluna
        for c in columns:
            # quantidade de aparicoes de cada letra
            letter_count = tp.Get_letter_count(c)
            #print(f'letter count = {letter_count}')
            # indice de coincidencia do grupo
            index += Index_coincidence(letter_count, len(ciphertext))
            #print(f'ic = {ic(letter_count, len(ciphertext))}')

        # indice de coincidencia medio do grupo
        avarege_index = index/len(columns)

        #print(f'avarege index = {avarege_index}')

        # menor indice de coincidencia medio
        if (IC_ENG - avarege_index) < minimum:
            minimum = IC_ENG - avarege_index
            key_length = possible_key_length
        
    return key_length


"""
decifrar mensagem (sem chave)
"""
def Decrypt(ciphertext):
    # comprimento da chave
    key_length = Keyword_lenght(ciphertext)

    # chave de cifracao
    key = Key(ciphertext, key_length)

    #print(f'key length = {kl}')
    #print(f'key  = {key}')

    # decifra com a chave descoberta
    decrypted_ciphertext = Cipher_decipher(ciphertext, key, 'decypher')

    return decrypted_ciphertext