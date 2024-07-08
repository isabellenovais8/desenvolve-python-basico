exp_registrados = int(input("Quantidade de experimentos realizados: "))
total_cobaias = 0
cobaias_tipo = {'S': 0, 'R': 0, 'C': 0}

while exp_registrados > 0:
    quant , tipo = input("Digite a quantidade e o tipo de cobaia (S/R/C): ").split()
    quant = int(quant)

    total_cobaias += (quant)
    cobaias_tipo[tipo] += quant
    exp_registrados -= 1

print("Total de cobaias utilizadas: ", total_cobaias)
print(f"Total de coelhos: {cobaias_tipo['C']}")
print(f"Total de ratos: {cobaias_tipo['R']}")
print(f"Total de sapos: {cobaias_tipo['S']}")
print(f"Percentual de coelhos: {cobaias_tipo['C'] / total_cobaias:.2%}")
print(f"Percentual de ratos: {cobaias_tipo['R'] / total_cobaias:.2%}")
print(f"Percentual de sapos: {cobaias_tipo['S'] / total_cobaias:.2%}")