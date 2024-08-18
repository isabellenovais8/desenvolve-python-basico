'''Desenvolva um programa que verifique se uma frase fornecida pelo usuário é um palíndromo (ou seja, lida
da mesma forma de trás para frente). Ignore espaços em branco ou sinais de pontuação, e considere maiúsculas
e minúsculas da mesma forma. Seu programa deve continuar rodando até que o usuário digite "Fim".Ex:

Digite uma frase (digite "fim" para encerrar): Radar
"Radar" é palíndromo
Digite uma frase (digite "fim" para encerrar): Bom dia!
"Bom dia!" não é palíndromo
Digite uma frase (digite "fim" para encerrar): Ame o poema
"Ame o poema" é palíndromo
Digite uma frase (digite "fim" para encerrar): A Daniela ama a lei? Nada!
"A Daniela ama a lei? Nada!" é palíndromo
Digite uma frase (digite "fim" para encerrar): fim '''

def verifica_palindromo(frase):
    frase = "".join(c.lower() for c in frase if c.isalnum())
    invertida = frase[::-1]
    return frase == invertida

while True:
    frase = input("Digite uma frase: ")
    if frase.lower() == "fim":
        break
    if verifica_palindromo(frase):
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo.")