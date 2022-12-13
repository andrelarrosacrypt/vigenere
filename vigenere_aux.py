""" versao auxiliar """

alphabet_len = 26

def pad_key(plaintext, key):
    padded_key = ''
    i = 0

    for char in plaintext:
        if char.isalpha():
            padded_key += key[i % len(key)]
        else:
            padded_key += ' '
        
        i += 1
    
    return padded_key

def encrypt_decrypt_char(plaintext_char, key_char, mode = 'encrypt'):
    if plaintext_char.isalpha():
        first_alphabetic_letter = 'a'
        #print(f'ord a: {ord(first_alphabetic_letter)}')

        if plaintext_char.isupper():
            first_alphabetic_letter = 'A'
            #print(f'ord A: {ord(first_alphabetic_letter)}')

        old_char_position = ord(plaintext_char) - ord(first_alphabetic_letter)
        key_char_position = ord(key_char.lower()) - ord('a')

        #print(f'ord char: {old_char_position}')

        if mode == 'encrypt':
            new_char_position = (old_char_position + key_char_position) % alphabet_len
            print(f'ord char: {new_char_position}')
        else:
            new_char_position = (old_char_position - key_char_position + 26) % alphabet_len

        return chr(new_char_position + ord(first_alphabetic_letter))
    else:
        return plaintext_char

def encrypt(plaintext, key):
    ciphertext = ''
    padded_key = pad_key(plaintext, key)


    for plaintext_char, key_char in zip(plaintext, padded_key):
        ciphertext += encrypt_decrypt_char(plaintext_char, key_char)
    
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    padded_key = pad_key(ciphertext, key)

    for ciphertext_char, key_char in zip(ciphertext, padded_key):
        plaintext += encrypt_decrypt_char(ciphertext_char, key_char, mode = 'decrypt')
    
    return plaintext


plaitext = input('message: ')
key = input('key: ')

ciphertext = encrypt(plaitext, key)
decrypted_plaintext = decrypt(ciphertext, key)

print(f'ciphertext: {ciphertext}')
print(f'decrypted plaintext: {decrypted_plaintext}')