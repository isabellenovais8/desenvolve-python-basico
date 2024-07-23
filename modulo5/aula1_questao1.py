'''Desenvolva um programa em Python que peça ao usuário para inserir dois números decimais e calcule a diferença absoluta
entre esses dois números. Utilize a função nativa abs para garantir que o resultado seja sempre positivo e round para
arredondar o resultado para duas casas decimais.'''

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
dif = abs(num1 - num2)

print(f"A diferença absoluta entre os números é: {round(dif, 2)}")