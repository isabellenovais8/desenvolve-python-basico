'''Dada uma string e uma palavra objetivo, encontre todos os anagramas da palavra objetivo. Anagramas são
palavras com os mesmos caracteres rearranjados.'''

def cont_caracteres(s):
    # Conta a frequência dos caracteres
    cont = {}
    for letra in s:
        cont[letra] = cont.get(letra, 0) + 1
    return cont

def encontra_anagrama(frase, alvo):
    alvo = alvo.lower()
    alvo_tamanho = len(alvo)
    cont_alvo = cont_caracteres(alvo)
    anagrama = []

    # Busca palavras parecidas
    for i in range(len(frase) - alvo_tamanho + 1):
        palavras = frase[i:i + alvo_tamanho].lower()
        if cont_caracteres(palavras) == cont_alvo:
            anagrama.append(palavras)

    return anagrama

frase = input("Digite a frase: ")
palavra_alvo = input("Digite a palavra objetivo: ")

anagramas = encontra_anagrama(frase, palavra_alvo)
print("Anagramas encontrados:", anagramas)
