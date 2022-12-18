"""
    UnB
    CIC0201 - Seguranca Computacional - 2022/2
    Andre Larrosa Chimpliganond
    190010321
"""

"""
imports
"""
from cipher_decipher import Cipher_decipher
from sys import maxsize
from constants import IC_ENG, IC_PORT, MAX_KEY_LENGTH
import text_processing as tp
from collections import Counter
import string

"""
calcula a distribuicao qui quadrado para cada possivel decifracao
https://en.wikipedia.org/wiki/Chi-squared_distribution
"""
def Chi_square(text, possible_decyphered_text, mode):
    text_len = len(text)
    expected_letters_count = tp.Get_exp_letter_count(text_len, mode)
    actual_letters_count = tp.Get_letter_count(possible_decyphered_text)

    normalized_error = Counter()

    # calcula o erro normalizado entre as quantidades esperadas de cada letra e a quantidade real
    for l in actual_letters_count:
        # error = actual_letters_count - expected_letters_count
        # sq_error = error^2
        normalized_error[l] = pow( (actual_letters_count[l] - expected_letters_count[l]), 2 ) / expected_letters_count[l]

    # soma de todos os erros quadraticos normalizados
    chi_square = sum(normalized_error.values())

    return chi_square

"""
descobre a letra que foi usada para cifrar o grupo
"""
def Key_letter(group, mode):
    chi_square = Counter()

    # dentre todas as letras do alfabeto, qual provavelmente cifrou esse grupo
    for index, letter in enumerate(string.ascii_lowercase):
        # grupo possivelmente decifrado
        possible_decyphered_group = Cipher_decipher(group, letter, 'decypher')
        # lista com todos ao chi_square para todas as letras do alfabeto
        chi_square[letter] = Chi_square(group, possible_decyphered_group, mode)
    
    # menor distribuicao qui quadrado e a letra que provavelmente cifrou o grupo
    key_letter = sorted(chi_square, key=chi_square.get, reverse=False)[0]

    return key_letter

"""
recupera a chave que decifra o texto
"""
def Key(ciphertext, key_length, mode):
    groups = tp.Get_groups(ciphertext, key_length)

    key = ''
    # recupera letra por letra
    for g in groups:
        key += Key_letter(g, mode)

    return key

"""
calcula o indice de coincidencia do grupo
https://en.wikipedia.org/wiki/Index_of_coincidence
"""
def Index_coincidence(letter_count, text_size):
    num = 0

    # para cada letra pertencente ao grupo
    for l in letter_count:
        num += letter_count[l] * (letter_count[l] - 1)

    den = text_size * (text_size-1)

    if den == 0:
        index_coincidence = num
    else:
        index_coincidence = num/den

    return index_coincidence

"""
descobre o comprimento da palavra chave usando indice de coincidencia
"""
def Keyword_lenght(ciphertext, mode):
    groups = []
    minimum = maxsize
    key_length = 0

    # descobre o comprimento mais provavel da chave
    for possible_key_length in range(1, MAX_KEY_LENGTH+1):
        groups = tp.Get_groups(ciphertext, possible_key_length)
        index_total = 0
        letter_count = Counter()

        # para cada grupo
        for g in groups:
            # numero de aparicoes de cada letra no grupo
            letter_count = tp.Get_letter_count(g)
            # indice de coincidencia total dos grupos
            index_total += Index_coincidence(letter_count, len(g))

        # indice de coincidencia medio do grupo
        avarege_index = index_total/len(groups)

        # indice de coincidencia medio deve ser o mais proximo do indice da lingua inglesa
        if mode == 'english':
            if (abs(IC_ENG - avarege_index)) < minimum:
                minimum = abs(IC_ENG - avarege_index)
                key_length = possible_key_length
        # indice de coincidencia medio mais proximo do indice da lingua portuguesa
        else:
            if (abs(IC_PORT - avarege_index)) < minimum:
                minimum = abs(IC_PORT - avarege_index)
                key_length = possible_key_length
        
    return key_length

"""
gerencia as etapadas de decifracao da mensagem
"""
def Decrypt(ciphertext, mode):
    # comprimento da chave
    key_length = Keyword_lenght(ciphertext.lower(), mode)

    # recupera a chave de cifracao
    key = Key(ciphertext, key_length, mode)

    print(f'\nCHAVE DESCOBERTA  = {key}')

    # decifra com a chave descoberta
    decrypted_ciphertext = Cipher_decipher(ciphertext, key, 'decypher')

    return decrypted_ciphertext