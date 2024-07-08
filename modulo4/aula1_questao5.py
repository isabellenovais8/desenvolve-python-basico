n = int(input("Digite a quantidade de valores: "))
idades = []
total_idades = 0

while n > 0:
    idade = int(input("Digite a idade: "))
    idades.append(idade)
    total_idades += idade
    n -= 1

media = total_idades / len(idades)
print("A média das idades é: ",media)