""" minha versao """

# tamanho do alfabeto
alphabet_len = 26

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
programa principal
"""

message = input('Insira mensagem que deseja cifrar: ')
key = input('Insira chave de cifracao (somente letras) ')

cipher_message = cipher_decipher(message, key, mode = 'cipher')
decipher_message = cipher_decipher(cipher_message, key, mode = 'decipher')

print(f'mensagem cifrada: {cipher_message}')
print(f'mensagem decifrada: {decipher_message}')