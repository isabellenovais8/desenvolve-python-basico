'''Crie a função encrypt() que recebe uma lista de strings e retorna os nomes criptografados, bem como a chave
da criptografia. Regras:
    - Chave de criptografia: gere um valor n aleatório entre 1 e 10
    - Substitua cada caracter c pelo caracter c + n. Trabalharemos apenas com o intervalo de caracteres visíveis
    (entre 33 e 126 na tabela Unicode)'''

import random

def encrypt(lista_strings):
    chave = random.randint(1, 10)
    
    def encrypt_string(s, chave):
        encryptado = []
        for letra in s:
            cod_original = ord(letra)
            novo_cod = cod_original + chave
            if novo_cod > 126:
                novo_cod = 33 + (novo_cod - 127)
            encryptado.append(chr(novo_cod))
        return ''.join(encryptado)
    
    letra_encryptada = [encrypt_string(s, chave) for s in lista_strings]
    
    return letra_encryptada, chave

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nome_encryptado, chave_encryptada = encrypt(nomes)

print(f"Nomes: {nomes}")
print(f"Chave de criptografia: {chave_encryptada}")
print(f"Nomes criptografados: {nome_encryptado}")