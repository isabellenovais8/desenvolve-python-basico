'''
2) Dando continuidade à questão anterior, um outro bar permite a entrada de grupos onde pelo menos uma pessoa é maior 
de idade (ficando responsável pelas outras). Ajuste sua resposta da questão anterior, ainda solicitando as idades de 
Juliana e Cris, mas ajustando a expressão para esse novo cenário, imprimindo True se puderem entrar no bar, e False 
caso contrário.
'''

idade_Juliana = int(input("Digite sua idade, Juliana: "))
idade_Cris = int(input("Digite sua idade, Cris: "))

entrada = (idade_Juliana > 17) or (idade_Cris > 17)

print(entrada)

if (entrada == True): {
    print("Entrada permitida")
}
else: {
    print("Entrada não permitida")
}