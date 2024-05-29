'''
5) Solicite de um usuário seu gênero ("M" ou "F"), sua idade e seu tempo de serviço (em anos) e escreva uma expressão 
que imprima True se a pessoa já pode se aposentar, ou False caso contrário, de acordo com as seguintes regras:

A: Para mulheres, ter mais de 60 anos. Para homens, 65.
B: Ou ter trabalhado pelo menos 30 anos
C: Ou ter 60 anos  e trabalhado pelo menos 25.
'''

genero = input("Digite seu genero (M ou F): ")
idade = int(input("Digite sua idade: "))
tempo_serv = int(input("Digite o tempo de serviço (em anos): "))

regra_m = (genero == "M" or genero == "m") and (idade > 65) or (tempo_serv >= 30) or (idade >= 60 and tempo_serv >= 25)
regra_f = (genero == "F" or genero == "f") and (idade > 60) or (tempo_serv >= 30) or (idade >= 60 and tempo_serv >= 25)

if ((regra_m == True) or (regra_f == True)): {
    print(True, "Você já pode se aposentar.")
}
else: {
    print(False, "Você ainda não pode se aposentar.")
}