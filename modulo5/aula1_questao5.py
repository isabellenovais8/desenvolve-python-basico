'''Você está trabalhando em um sistema de mensagens instantâneas, que deve permitir o uso de emojis nas conversas entre
pessoas. Faça: No terminal, instale a biblioteca emoji usando o gerenciador de pacotes pip
    $ pip install emoji
    Conheça a função emoji.emojize()
Seu programa deve apresentar para o usuário a lista de emojis disponíveis com o texto correspondente a cada emoji. Em
seguida, solicite uma frase codificada ao usuário e apresente ela decodificada com a visualização de emojis (emojizada).
A seguir um exemplo de interação, com uma lista de emojis sugeridos. Você pode consultar o texto que codifica outros
emojis indo nessa página e passando o mouse por cima do emoji desejado.'''

import emoji

print("Emojis disponíveis: ")
print("❤️  - :red_heart:")
print("👍 - :thumbs_up:")
print("🤔 - :thinking_face:")
print("🤓 - :nerd_face:")
print("💢 - :anger_symbol:")
print("✅ - :check_mark_button:")
print(" ")

frase = input("Digite uma frase e ela será emojizada: ")
print("Frase emojizada: ")
print(emoji.emojize(frase))