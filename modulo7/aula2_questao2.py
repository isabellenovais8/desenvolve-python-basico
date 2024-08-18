'''Desenvolva um programa que solicite ao usuário inserir uma frase e substitua todas as ocorrências de
vogal por "*".
Ex:
Digite uma frase: O rato roeu a roupa do rei
Frase modificada: * r*t* r*** * r**p* d* r** '''

def modifica_frase(frase):
    vogais = "aeiouAEIOU"
    nova_frase = ""
    for letra in frase:
        if letra in vogais:
            nova_frase += "*"
        else:
            nova_frase += letra
    return nova_frase

frase = input("Digite uma frase: ")
frase_modificada = modifica_frase(frase)
print(f"Frase modificada: {frase_modificada}")