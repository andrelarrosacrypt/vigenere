"""
imports
"""
from cipher_decipher import Cipher_decipher
from decrypt import Decrypt


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
def factors(distances):
    factors_occurrences = []

    for f in range(3, ct.N_FACTOR):   # fatores de 3 a um numero definido
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

"""
programa principal
"""

"""
# cifracao e decifracao com chave
message = input('Insira mensagem que deseja cifrar: ')
key = input('Insira chave de cifracao (somente letras) ')

enciphered_message = Cipher_decipher(message, key, mode = 'cipher')
deciphered_message = Cipher_decipher(enciphered_message, key, mode = 'decipher')

print(f'\nmensagem cifrada: {enciphered_message}')
print(f'mensagem decifrada: {deciphered_message}')
"""

# decifracao (sem chave)
ciphertext = input('\nInsira mensagem que deseja decifrar: ')

decrypted_ciphertext = Decrypt(ciphertext)

print(f'\nmensagem decifrada: {decrypted_ciphertext}')
