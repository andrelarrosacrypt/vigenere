"""
constantes
"""
#N_FACTOR = 20

# indice de coincidencia na lingua inglesa
IC_ENG = 0.0665
# indice de coincidencia na lingua portuguesa
IC_PORT = 0.0746
# tamanho do alfabeto
ALPHABET_LEN = 26
# tamanho maximo esperado do chave
MAX_KEY_LENGTH = 20

# frequencia de aparicoes das letras do alfabeto em um texto em ingles
FREQ_ENG = {    'a': 0.08167,
                'b': 0.01492,
                'c': 0.02782,
                'd': 0.04253,
                'e': 0.12702,
                'f': 0.02228,
                'g': 0.02015,
                'h': 0.06094,
                'i': 0.06966,
                'j': 0.00153,
                'k': 0.00772,
                'l': 0.04025,
                'm': 0.02406,
                'n': 0.06749,
                'o': 0.07507,
                'p': 0.01929,
                'q': 0.00095,
                'r': 0.05987,
                's': 0.06327,
                't': 0.09056,
                'u': 0.02758,
                'v': 0.00978,
                'w': 0.02360,
                'x': 0.00150,
                'y': 0.01974,
                'z': 0.00074}

# frequencia de aparicoes das letras do alfabeto em um texto em portugues
FREQ_PORT = {   'a': 0.1463,
                'b': 0.0104,
                'c': 0.0388,
                'd': 0.0499,
                'e': 0.1257,
                'f': 0.0102,
                'g': 0.0130,
                'h': 0.0128,
                'i': 0.0618,
                'j': 0.0040,
                'k': 0.0002,
                'l': 0.0278,
                'm': 0.0474,
                'n': 0.0505,
                'o': 0.1073,
                'p': 0.0252,
                'q': 0.0120,
                'r': 0.0653,
                's': 0.0781,
                't': 0.0434,
                'u': 0.0463,
                'v': 0.0167,
                'w': 0.0001,
                'x': 0.0021,
                'y': 0.0001,
                'z': 0.0047}