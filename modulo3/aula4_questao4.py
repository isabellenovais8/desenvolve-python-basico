'''4) Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base na distância
e no peso do pacote. Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote em
quilogramas. O programa deve calcular e imprimir o valor do frete de acordo com as seguintes regras:
Distância até 100 km: R$1 por kg.
Distância entre 101 e 300 km: R$1.50 por kg.
Distância acima de 300 km: R$2 por kg.
Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg '''

distancia = int(input("Digite a distância da entrega (KM): "))
peso = float(input("Digite o peso do pacote (KG): "))
frete100 = peso * 1
frete101 = peso * 1.5
frete300 = peso * 2

taxa100 = (frete100 + 10) if peso > 10 else frete100
taxa101 = (frete101 + 10) if peso > 10 else frete101
taxa300 = (frete300 + 10) if peso > 10 else frete300

if (distancia <= 100): {
    print("Valor do frete: ", taxa100)
}
elif ((distancia > 100) and (distancia <= 300)): {
    print("Valor do frete: ", taxa101)
}
elif (distancia > 300): {
    print("Valor do frete: ", taxa300)
}