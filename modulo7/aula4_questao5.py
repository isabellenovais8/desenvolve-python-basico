'''A extensão ".csv" significa "comma-separated values" ou "valores separados por vírgula". É a extensão
utilizada por sistemas de gerência de tabelas como o Microsoft Excel ou Google Sheets. Nesse exercício vamos
criar uma planilha com dados sobre livros que você já leu ou gostaria de ler. Siga as instruções.
    - Selecione pelo menos 10 livros que você leu ou gostaria de ler. Você deve reunir as seguintes
    informações: título, autor, ano de publicação e número de páginas.
    - No Python, crie um arquivo chamado "meus_livros.csv", aberto para escrita.
    - Na primeira linha escreva os títulos da planilha separados por vírgula (sem espaço em branco). Os
    títulos são: "Título", "Autor", "Ano de publicação" e "Número de páginas". Lembre de finalizar a linha
    com uma quebra de linha.
    - A partir da segunda linha escreva as informações de cada livro que você levantou, separando cada
    informação por uma vírgula (sem espaço em branco). Lembre de finalizar cada linha com uma quebra de linha.
    - Feche o arquivo para salvá-lo e abra com a ferramenta de planilhas de sua escolha. Como você já tem
    conta no Google, sugiro abrir com o Google Sheets.
Seu arquivo deve ser aberto como uma planilha parecida com a imagem anexada neste exercício.'''

#Livros lidos ou para ler
livros = [
    {"Título": "A Sorte Segue a Coragem", "Autor": "Mário Sérgio Cortella", "Ano de publicação": 2018, "Número de páginas": 192},
    {"Título": "Viver em Paz Para Morrer em Paz", "Autor": "Mário Sérgio Cortella", "Ano de publicação": 2017, "Número de páginas": 176},
    {"Título": "Mindset", "Autor": "Carol S. Dweck", "Ano de publicação": 2017, "Número de páginas": 312},
    {"Título": "O Poder do Hábito", "Autor": "Charles Duhigg", "Ano de publicação": 2012, "Número de páginas": 408},
    {"Título": "A Psicologia Financeira", "Autor": "Morgan Housel", "Ano de publicação": 2021, "Número de páginas": 304},
    {"Título": "Essencialismo", "Autor": "Greg McKeown", "Ano de publicação": 2015, "Número de páginas": 272},
    {"Título": "Como Fazer Amigos e Influenciar Pessoas", "Autor": "Dale Carnegie", "Ano de publicação": 2019, "Número de páginas": 256},
    {"Título": "O Jeito Harvard de Ser Feliz", "Autor": "Shawn Achor", "Ano de publicação": 2012, "Número de páginas": 216},
    {"Título": "Mais Esperto que o Diabo", "Autor": "Napoleon Hill", "Ano de publicação": 2014, "Número de páginas": 208},
    {"Título": "O Monge e o Executivo", "Autor": "James C Hunter", "Ano de publicação": 1989, "Número de páginas": 144}
]

# Cria o arquivo "meus_livros.csv" e escreve os títulos das colunas
with open("meus_livros.csv", "w", encoding="utf-8") as arquivo:
    arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")

    # Escreve as informações de cada livro
    for livro in livros:
        linha = f"{livro['Título']},{livro['Autor']},{livro['Ano de publicação']},{livro['Número de páginas']}\n"
        arquivo.write(linha)

print("Arquivo 'meus_livros.csv' criado com sucesso!")