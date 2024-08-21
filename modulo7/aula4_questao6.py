'''Vamos descobrir as músicas mais populares do Spotify nos últimos 10 anos!
Crie uma conta no Kaggle, uma das principais plataformas de ciência de dados e aprendizado de máquina. Em disciplinas avançadas vamos trabalhar com bases de dados provenientes de lá! (http://kaggle.com/)
Baixe o arquivo spotify-2023.csv no final da página que apresenta os dados: https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023
No Python, abra o arquivo para leitura e imprima as cinco primeiras linhas
Ao abrir o arquivo, defina o parâmetro encoding='latin-1'  na função open
Após compreender a estrutura do arquivo (divisão em colunas, caracter separador de coluna, etc.) passamos para a etapa de extração de informações.
O arquivo está estruturado da seguinte forma: cada linha representa uma música e contém as seguintes informações separadas por vírgula (CSV):

track_name,artist(s)_name,artist_count,released_year,released_month,released_day,in_spotify_playlists,in_spotify_charts,streams,in_apple_playlists

Usaremos apenas informações das colunas:
track_name: Nome da música
artist(s)_name: Nome do artista
artist_count: Número de artistas listados em artist(s)_name
released_year: Ano de lançamento
streams: Número de vezes que a música foi tocada no Spotify
Você deve criar um script Python para processar esse arquivo e gerar uma lista com 10 elementos, cada qual representando a música mais tocada de cada ano no intervalo de 2012 a 2022. Considere somente músicas dentro do intervalo solicitado. Cada elemento da lista produzida deve conter as seguintes informações:

[track_name, artist(s)_name, released_year, streams]

Essa atividade tem alguns desafios. Assim como as colunas da tabela são separadas por vírgulas, músicas com mais de um artista (artist_count>1) terá o campo artist(s)_name entre aspas com o nome dos artistas separado por vírgulas. 

Ex: Seven (feat. Latto) (Explicit Ver.),"Latto, Jung Kook",2,2023, …

Há também nomes de músicas entre aspas por conter caracteres especiais como vírgulas ou aspas. 

Ex: "Peso Pluma: Bzrp Music Sessions,Vol.55","Bizarrap,Peso Pluma",2,2023,

Você deve ignorar essas linhas, e terá portanto que propor uma verificação para identificá-las.

Ao final imprima a lista produzida. Ex:
[ ['When I Was Your Man', 'Bruno Mars', 2012, 1661187319],
 ['I Wanna Be Yours', 'Arctic Monkeys', 2013, 1297026226],
 ...,
 ['As It Was', 'Harry Styles', 2022, 2513188493] ]'''

import csv

# Lê o arquivo
def ler_arquivo_csv(spotify):
    with open('spotify-2023.csv', 'r', encoding='latin-1') as arquivo:
        leitor = csv.reader(arquivo)
        cabecalho = next(leitor)
        musicas = []
        for linha in leitor:
            try:
                track_name, artist_name, artist_count, released_year, _, _, _, _, streams, _ = linha
                released_year = int(released_year)
                streams = int(streams)
                # Filtra as músicas no intervalo de 2012 a 2022
                if 2012 <= released_year <= 2022:
                    musicas.append((track_name, artist_name, released_year, streams))
            except ValueError:
                pass
        return musicas

# Filtra músicas com mais de um artista e nomes entre aspas
def filtrar_musicas(musicas):
    resultado = []
    for track_name, artist_name, released_year, streams in musicas:
        if ',' in artist_name or '"' in track_name:
            continue
        resultado.append([track_name, artist_name, released_year, streams])
    return resultado

# Carrega o arquivo e filtra as músicas
spotify = open('spotify-2023.csv')
musicas = ler_arquivo_csv(spotify)
musicas_filtradas = filtrar_musicas(musicas)
spotify.close()

# Ordena as músicas por ano e streams
musicas_filtradas.sort(key=lambda x: (x[2], -x[3]))

# Seleciona as 10 músicas mais tocadas de cada ano
musicas_por_ano = {}
for musica in musicas_filtradas:
    track_name, artist_name, released_year, streams = musica
    if released_year not in musicas_por_ano:
        musicas_por_ano[released_year] = []
    if len(musicas_por_ano[released_year]) < 10:
        musicas_por_ano[released_year].append([track_name, artist_name, released_year, streams])

# Lista final de músicas
for ano, top10 in musicas_por_ano.items():
    print(f'Ano {ano}:')
    for musica in top10:
        print(f"Música: {musica}")