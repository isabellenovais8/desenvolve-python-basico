'''Baixe o arquivo contendo o roteiro do filme brasileiro "Estômago" (link a seguir) e salve em seu computador
com o nome "estomago.txt". 

Link: https://aplauso.imprensaoficial.com.br/edicoes/12.0.813.502/12.0.813.502.txt

Em seguida crie um script em Python que abra o arquivo para leitura e imprima: 
    O texto das primeiras 25 linhas
    O número de linhas do arquivo
    A linha com maior número de caracteres
    O número de menções aos nomes dos personagens "Nonato" e "Íria" (inclua todas as variações de maiúsculas e
minúsculas e atenção para não incluir a substring "iria" se ela fizer parte de outras palavras).'''

# O texto das primeiras 25 linhas
f = open('estomago.txt')
texto_linhas = f.readlines()
print(texto_linhas[:25])
f.close()
print("-" * 30)

# O número de linhas do arquivo
f = open('estomago.txt')
linhas = f.readlines()
print("Quantidade de linhas: ", len(linhas))
f.close()
print("-" * 30)

#A linha com maior número de caracteres
with open("estomago.txt", "r") as arquivo:
    maior_tamanho = 0
    linha_maior_tamanho = ""

    num_nonato = 0
    num_iria = 0

    for linha in arquivo:
        #Encontra o número de menções aos nomes dos personagens
        num_nonato += linha.lower().count("nonato")
        num_iria += linha.lower().count("íria")

        #Encontra a linha com maior número de caracteres
        tamanho_atual = len(linha)
        if tamanho_atual > maior_tamanho:
            maior_tamanho = tamanho_atual
            linha_maior_tamanho = linha

print(f"Linha com maior número de caracteres:\n{linha_maior_tamanho.strip()}")
print("-" * 30)

# O número de menções aos nomes dos personagens "Nonato" e "Íria" (inclua todas as variações de maiúsculas e
# minúsculas e atenção para não incluir a substring "iria" se ela fizer parte de outras palavras)
print(f"Número de menções a Nonato: {num_nonato}")
print(f"Número de menções a Íria: {num_iria}")