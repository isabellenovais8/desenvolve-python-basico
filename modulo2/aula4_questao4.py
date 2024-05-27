''' 4) Escreva um programa que leia um valor inteiro referente a uma quantia em reais e calcule a menor quantidade 
possível de notas necessárias para pagar aquele valor. As notas possíveis são: 100, 50, 20, 10, 5, 2, 1. A saída 
deve estar formatada exatamente como indicado. 

Entrada: 576

Saída:
5 nota(s) de R$100,00
1 nota(s) de R$50,00
1 nota(s) de R$20,00
0 nota(s) de R$10,00
1 nota(s) de R$5,00
0 nota(s) de R$2,00
1 nota(s) de R$1,00 '''

total_reais = int(input("Quantidade em reais: "))

notas_100 = total_reais // 100
total_reais = total_reais % 100

notas_50 = total_reais // 50
total_reais = total_reais % 50

notas_20 = total_reais // 20
total_reais = total_reais % 20

notas_10 = total_reais // 10
total_reais = total_reais % 10

notas_05 = total_reais // 5
total_reais = total_reais % 5

notas_02 = total_reais // 2
total_reais = total_reais % 2

notas_01 = total_reais // 1

print(f"{notas_100} nota(s) de R$ 100,00")
print(f"{notas_50:.0f} nota(s) de R$ 50,00")
print(f"{notas_20:.0f} nota(s) de R$ 20,00")
print(f"{notas_10:.0f} nota(s) de R$ 10,00")
print(f"{notas_05:.0f} nota(s) de R$ 5,00")
print(f"{notas_02:.0f} nota(s) de R$ 2,00")
print(f"{notas_01:.0f} nota(s) de R$ 1,00")