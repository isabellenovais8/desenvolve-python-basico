'''Escreva um script que dado uma frase conta os espaços em branco.'''

def conta_espacos(frase):
    return frase.count(' ')

frase = input("Digite a frase: ")

cont_space = conta_espacos(frase)

print(f"Espaços em branco: {cont_space}")