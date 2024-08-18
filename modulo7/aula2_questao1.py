'''Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome
do mês por extenso. 
Dica: usando listas você não precisa fazer um "if" para cada mês.
Ex:
Digite uma data de nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973.'''

def obtem_mes(data_nascimento):
    dia, mes, ano = map(int, data_nascimento.split("/"))
    
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", \
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    
    nome_mes = meses[mes - 1]

    print(f"Você nasceu em {dia} de {nome_mes} de {ano}")

data_nascimento = input("Digite uma data de nascimento: ")
frase = obtem_mes(data_nascimento)
