'''2) Dada uma lista de endereços web (URLs) que sempre começam com "www." e sempre terminam com ".com", use o
conceito de fatiamento de listas para criar uma lista domínios com o nome principal de todas as URLs, conforme
exemplo a seguir.

URLs: ["www.google.com, www.gmail.com, www.github.com, www.reddit.com, www.yahoo.com]
dominios:  ["google", "gmail", "github", "reddit", "yahoo"]'''

urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]
dominios = [lista[4:-4] for lista in urls]

print(f"Lista de URLs: {urls}")
print(f"Lista de domínios: {dominios}")