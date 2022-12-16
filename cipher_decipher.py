from constants import ALPHABET_LEN

"""
cifracao ou decifracao
"""
def Cipher_decipher_aux(text_char, key_char, mode):
    if text_char.isalpha():
        # posicao da primeira letra e usada como referencial para descobrir o caracter cifrada 
        if text_char.islower():
            m_first_letter = ord('a')
        else:
            m_first_letter = ord('A')
        
        if key_char.islower():
            k_first_letter = ord('a')
        else:
            k_first_letter = ord('A')

        # posicoes relativas a primeira letra
        text_char_pos = ord(text_char) - m_first_letter
        key_char_pos = ord(key_char) - k_first_letter

        # posicao no alfabeto do novo caracter para cifracao ou decifracao
        if mode == 'cipher':
            # cifracao
            new_text_char_pos = (text_char_pos + key_char_pos) % ALPHABET_LEN
        else:
            # decifracao
            new_text_char_pos = (text_char_pos - key_char_pos + ALPHABET_LEN) % ALPHABET_LEN
    else:
        # nao cifra caracteres nao alfabeticos, nao avanca nos caracteres da chave
        return (text_char,0)

    # retorna o caracter relativo a nova posicao
    new_text_char = chr(new_text_char_pos + m_first_letter)

    # avanca nos acaracteres da chave
    return (new_text_char,1)


"""
gerencia a funcao de cifracao e decifracao (cipher_decipher_aux)
"""
def Cipher_decipher(text, key, mode):
    new_text = ''
    i = 0
    
    for text_char in text:
        # loop dos caracteres da chave
        key_char = key[i%len(key)]
        text_code = Cipher_decipher_aux(text_char, key_char, mode)
        # primeira parte da tupla tem o caracter
        new_text += text_code[0]
        # segunda parte da tupla tem o codigo que indica se e preciso ou nao avancar nos caracteres da chave
        i += text_code[1]

    return new_text