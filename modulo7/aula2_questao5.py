'''De acordo com uma pesquisa do linguista Matt Davis, o cérebro humano consegue ler palavras com as letras
embaralhadas, contanto que a primeira e a última letra estejam no lugar correto. Implemente uma função
chamada embaralhar_palavras() para ajudar a testar a hipótese do Matt Davis. Sua função vai receber uma
frase, embaralhar as letras internas de cada palavra e retornar a frase modificada. Dica: use a biblioteca
random.

Complete o seguinte código:
def embaralhar_palavras(frase):
    #### Escreva a função

# Exemplo de uso:
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
# Possível saída: "Ptohyn é uma lignaugem de prarmoagãço" '''

import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    nova_frase = []

    for palavra in palavras:
        if len(palavra) > 2:
            letras = list(palavra[1:-1])
            random.shuffle(letras)
            palavra_embaralhada = palavra[0] + "".join(letras) + palavra[-1]
            nova_frase.append(palavra_embaralhada)
        else:
            nova_frase.append(palavra)

    return " ".join(nova_frase)    

frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)