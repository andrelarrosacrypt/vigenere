# tamanho do alfabeto
alphabet_len = 26
n_factors = 20

"""
faz a cifracao ou decifracao dependendo so modo (mode) escolhido
"""

def cipher_decipher_aux(message_char, key_char, mode):
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
            new_message_char_pos = (message_char_pos + key_char_pos) % alphabet_len
        else:
            new_message_char_pos = (message_char_pos - key_char_pos + alphabet_len) % alphabet_len
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

def cipher_decipher(text, key, mode):
    new_text = ''
    i = 0
    
    for text_char in text:
        # loop dos caracteres sa chave
        key_char = key[i%len(key)]
        text_code = cipher_decipher_aux(text_char, key_char, mode)
        # primeira parte da tupla tem o caracter
        new_text += text_code[0]
        # segunda parte da tupla tem o codigo que indica se e preciso ou nao avancar nos caracteres da chave
        i += text_code[1]

    return new_text


"""
def keyword_lenght(ciphertext):
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

    for f in range(3, n_factors):   # fatores de 3 a um numero definido
        count = 0
        for d in distances:
            if d%f == 0:    # verificamos se a distancia d e divisivel pelo fator f
                count += 1
        factors_occurrences.append((f, count))  # lista dos fatores e a quantidade de distanceias que eles dividem

    return factors_occurrences


def tuples(ciphertext):
    distance = []
    #list_strings = []
    i = 0
    
    while(i <= (len(ciphertext) - 3)): # < ou <=?
        flag_jumo_i = 0
        lenght_tuple = 3    # tamanho da tupla comeca com 3 e pode aumentar
        possible_tuple = ciphertext[i:i+lenght_tuple]

        for j in range((i+1), len(ciphertext)):
            if possible_tuple == ciphertext[j:j+lenght_tuple]: # se encontramos uma tupla repetida, aumentamos o tamamho da tupla
                #list_strings.append(possible_tuple)
                # acho que nao tem problema contabilizar duas vezes a mesma tupla
                flag_jumo_i = 1
                while (ciphertext[i:i+lenght_tuple] == ciphertext[j:j+lenght_tuple]) and (i+lenght_tuple < j): # precisa do 'if' ou pode ser so while
                    lenght_tuple += 1   # aumenta o tamano da tupla enquanto ambas forem iguais
                lenght_tuple -= 1   # se chegou aqui as tuplas passaram a ser diferentes, logo volta um passo no tamanho

                possible_tuple = ciphertext[i:i+lenght_tuple] # essa e a tupla. Precisa disso?

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


"""
descobrir o comprimento da palavra chave usando o metodo de Kasiski
"""
def keyword_lenght(ciphertext):
    tuples(ciphertext)


"""
decifrar mensagem sem chave
"""

def decrypt(ciphertext):
    keyword_lenght(ciphertext)


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


ciphertext = input('Insira mensagem que deseja decifrar: ')

decrypt(ciphertext)