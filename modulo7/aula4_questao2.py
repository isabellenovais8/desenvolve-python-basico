'''Escreva um script que leia o arquivo salvo no exercício anterior e salva em um novo arquivo "palavras.txt",
removendo todos os espaços em branco e caracteres não alfabéticos, e separando cada palavra em uma linha.
Ao final, imprima o conteúdo do arquivo "palavras.txt".
Ex:
Bom
dia
meu
nome
é
Davi'''

def limpar_palavra(palavra):
    return "".join(c for c in palavra if c.isalpha())

# Lê o conteúdo do arquivo "frase.txt"
try:
    with open("frase.txt", "r", encoding="utf-8") as arquivo_frase:
        conteudo = arquivo_frase.read()
except FileNotFoundError:
    print("Arquivo 'frase.txt' não encontrado.")

# Divide o conteúdo em palavras
palavras = conteudo.split()

# Limpa palavra e salva no arquivo "palavras.txt"
with open("palavras.txt", "w", encoding="utf-8") as arquivo_palavras:
    for palavra in palavras:
        palavra_limpa = limpar_palavra(palavra)
        if palavra_limpa:
            arquivo_palavras.write(palavra_limpa + "\n")

print("Conteúdo salvo em 'palavras.txt'.")

#Lê o arquivo e apresenta na tela
f = open('palavras.txt', 'r')
lines = f.read()
print(lines)
f.close()