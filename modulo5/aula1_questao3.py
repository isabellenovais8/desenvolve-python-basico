'''Escreva um programa em Python que utiliza a biblioteca random para gerar um número aleatório entre 1 e 10 e peça
ao usuário para adivinhar o número. Forneça feedback se o palpite é muito alto, muito baixo ou correto. Interrompa
a execução somente quando o usuário acertar o palpite.'''

import random

numero = random.randint(1, 10)
chute = 0

while chute != numero:
    chute = int(input("Adivinhe o número entre 1 e 10: "))
    if chute < numero:
        print("Chute muito baixo, tente novamente.")
    elif chute > numero:
        print("Chute muito alto, tente novamente.")
    else:
        print(f"Correto! O número é: {numero}.")