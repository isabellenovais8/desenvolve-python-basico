'''
4) Você é mestre de uma mesa de RPG e vai criar um sistema para validar uma ficha de personagem. Cada personagem tem 
uma classe específica com requisitos de atributos. Escreva um script que solicita a classe de personagem escolhida 
(guerreiro, mago ou arqueiro), os pontos de força e os pontos de magia atribuídos ao personagem. O programa deve 
imprimir True se os pontos de atributo são consistentes com a classe escolhida, seguindo as seguintes regras:

Guerreiro: Força deve ser igual ou superior a 15, Magia deve ser 10 ou menos.
Mago: Força deve ser 10 ou menos, Magia deve ser igual ou superior a 15.
Arqueiro: Força e Magia devem ser ambos superiores a 5, mas nenhum deles pode ser superior a 15.

O programa deve imprimir False se os pontos de atributo não são consistentes com a classe escolhida. Segue um exemplo 
de interação com seu código no terminal, com entradas de dados destacadas em negrito e as impressões de seu código 
em itálico.

Escolha a classe (guerreiro, mago ou arqueiro): mago
Digite os pontos de força (de 1 a 20): 8
Digite os pontos de magia (de 1 a 20): 17
Pontos de atributo consistentes com a classe escolhida: True
'''

classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ")
pt_forca = int(input("Digite os pontos de força (de 1 a 20): "))
pt_magia = int(input("Digite os pontos de magia (de 1 a 20): "))

guerreiro = (pt_forca >= 15) and (pt_magia <= 10)
mago = (pt_forca <= 10) and (pt_magia >= 15)
arqueiro = (pt_forca > 5 and pt_forca < 15) and (pt_magia > 5 and pt_magia < 15)

if ((classe == "guerreiro") and (guerreiro == True)): {
    print("Pontos de atributo consistentes com a classe escolhida: ", True)
}
elif ((classe == "mago") and (mago == True)): {
    print("Pontos de atributo consistentes com a classe escolhida: ", True)
}
elif ((classe == "arqueiro") and (arqueiro == True)): {
    print("Pontos de atributo consistentes com a classe escolhida: ", True)
}
else: {
    print("Pontos de atributo consistentes com a classe escolhida: ", False)
}