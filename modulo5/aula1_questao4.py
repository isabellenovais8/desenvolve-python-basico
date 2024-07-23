'''Escreva um programa em Python que utiliza a biblioteca datetime para exibir a data e hora atuais com a formatação
apresentada a seguir:

Você pode consultar esse tutorial da Alura sobre a biblioteca datetime. Existem várias maneiras de resolver essa questão.
Uma sugestão é: Função datetime.datetime.now() cujo retorno possui os atributos: day, month, year, hour, minute
Usar a formatação com f-strings no momento de imprimir. Atenção para os atributos que devem sempre ter 2 dígitos
precedidos por zero se necessário.'''

from datetime import datetime

data_atual = datetime.now()

data = data_atual.strftime("%d/%m/%Y")
hora = data_atual.strftime("%H:%M")

print(f"Data: {data}")
print(f"Hora: {hora}")