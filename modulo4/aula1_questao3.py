n1 = int(input("Digite n1: "))
n2 = int(input("Digite n2: "))
n3 = int(input("Digite n3: "))

m = ((n1 + n2 + n3) / 3)

while m >= 60:
    print("Aprovado!")
    print("Fim")
    break
    
while (m >=40 and m < 60):
    print("Recuperação!")
    print("Fim")
    break

while m < 40:
    print("Reprovado!")
    print("Fim")
    break