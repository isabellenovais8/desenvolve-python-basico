'''Vamos fazer o jogo da forca! Antes de programar crie e salve os seguintes arquivos na mesma pasta onde
você vai programar a solução: 
    - Crie um arquivo no seu computador chamado "gabarito_forca.txt" com uma lista de 10 palavras de sua
    escolha (separadas por quebras de linha, "\n"). Essas serão as opções de palavra do jogo.
    - Baixe o arquivo "gabarito_enforcado.txt": 
    https://github.com/camilalaranjeira/python-basico-exercicios/blob/main/modulo7/gabarito_enforcado.txt

Escreva um programa em Python para executar o jogo, de acordo com as definições:
    - Abra o arquivo "gabarito_forca.txt" e escolha aleatoriamente uma palavra;
    - Com o arquivo "gabarito_enforcado.txt", crie uma lista de strings com os estágios do enforcado;
    - No início exiba o número de letras da palavra sorteada como underscores;
    - Permita que o jogador insira letras para adivinhar a palavra;
    - Em caso de acerto, mostre o progresso do jogador substituindo os underscores correspondentes à letra
    digitada;
    - Em caso de erro, crie a função "imprime_enforcado()" que recebe um inteiro indicando o número de erros
    do jogador e imprime o enforcado correspondente;
    - Limite o número de tentativas para 6 (as partes do enforcado).'''

import random

# Abre o arquivo "gabarito_forca.txt"
def carregar_palavras():
    with open("gabarito_forca.txt", "r", encoding="utf-8") as arquivo:
        return arquivo.read().splitlines()

# Escolhe uma palavra aleatoriamente
def escolher_palavra(palavras):
    return random.choice(palavras)

#Abre o arquivo "gabarito_enforcado.txt"
def carregar_enforcado():
    with open("gabarito_enforcado.txt", "r", encoding="utf-8") as arquivo:
        return arquivo.read().splitlines()

#Apresenta a forca
def imprime_enforcado(tentativas):
    enforcado = carregar_enforcado()
    for i in range(3 - tentativas):
        print(enforcado[i])

# Inicializa o jogo
def jogar_forca():
    palavras = carregar_palavras()
    palavra_escolhida = escolher_palavra(palavras)
    letras_certas = set()
    tentativas = 6

    print("Bem-vindo ao Jogo da Forca!")
    print(f"A palavra tem {len(palavra_escolhida)} letras.")

    while tentativas > 0:
        letra = input("Digite uma letra: ").lower()

        if letra in palavra_escolhida:
            letras_certas.add(letra)
        else:
            tentativas -= 1
            imprime_enforcado(tentativas)

        # Exibe o progresso da palavra
        palavra_mostrada = "".join([letra if letra in letras_certas else "_" for letra in palavra_escolhida])
        print(f"Palavra: {palavra_mostrada}")

        if palavra_mostrada == palavra_escolhida:
            print("Parabéns! Você acertou a palavra.")
            break

    if tentativas == 0:
        print(f"Fim de jogo! A palavra era '{palavra_escolhida}'.")

# Inicia o jogo
jogar_forca()