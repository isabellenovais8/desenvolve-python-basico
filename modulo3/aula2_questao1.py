'''
1) Juliana e Cris querem entrar em um bar, mas só podem se ambos forem maiores de idade (>17). Escreva um programa
que solicite as idades de Juliana e Cris e imprima True se ambas forem maiores de 17 anos, indicando que podem entrar 
no bar, e False caso contrário.
'''

idade_Juliana = int(input("Digite sua idade, Juliana: "))
idade_Cris = int(input("Digite sua idade, Cris: "))

entrada = (idade_Cris > 17) and (idade_Juliana > 17)

print(entrada)

if (entrada == True): {
    print("Entrada permitida")
}
else: {
    print("Entrada não permitida")
}