'''1) Escreva um programa que lê dois números e informa se a sua soma é par ou ímpar. Critério: se o resto da divisão
do número por 2 for 0, o número é par, caso contrário é ímpar. Lembre-se do operador do python % que retorna o resto
de uma divisão.'''

num1 = int(input("Digite o número 1: "))
num2 = int(input("Digite o número 2: "))

soma = num1 + num2
divisao = soma % 2

if (divisao == 0): {
    print("Soma é par")
}
else: {
    print("Soma é ímpar")
}