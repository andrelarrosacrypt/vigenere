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
from decrypt import Decrypt

"""
programa principal
"""
# cifracao e decifracao com chave
message = input('INSIRA MENSAGEM QUE DESEJA CIFRAR: ')
key = input('INSIRA CHAVE DE CIFRACAO (somente letras): ')

ciphered_message = Cipher_decipher(message, key, mode = 'cipher')
deciphered_message = Cipher_decipher(ciphered_message, key, mode = 'decipher')

print(f'\nMENSAGEM CIFRADA:\n{ciphered_message}')
print(f'\nMENSAGEM DECIFRADA:\n{deciphered_message}')

# decifracao (ingles)
ciphertext_eng = input('\nINSIRA MENSAGEM QUE DESEJA DECIFRAR (ingles): ')

decrypted_ciphertext_eng = Decrypt(ciphertext_eng, mode = 'english')

print(f'\nMENSAGEM DECIFRADA:{decrypted_ciphertext_eng}')

# decifracao (portugues)
ciphertext_port = input('\nINSIRA MENSAGEM QUE DESEJA DECIFRAR (portugues): ')

decrypted_ciphertext_port = Decrypt(ciphertext_port, mode = 'portuguese')

print(f'\nMENSAGEM DECIFRADA:\n{decrypted_ciphertext_port}')