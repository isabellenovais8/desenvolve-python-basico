'''Desenvolva um validador de CPF. Solicite do usuário um CPF na forma XXX.XXX.XXX-XX (lido como string) e
imprima "Válido" ou "Inválido". 

O primeiro passo é calcular o primeiro dígito verificador. Separamos os primeiros 9 dígitos do CPF
(ex: 111.444.777) e multiplicamos cada um dos números, da direita para a esquerda por números crescentes a
partir do número 2, como no exemplo abaixo:

Em seguida somamos o resultado: 10+9+8+28+24+20+28+21+14 = 162
Pegamos o resultado e dividimos por 11:  162 / 11 = 14 com resto 8
    - Se o resto da divisão for menor que 2, então o dígito é igual a 0 (Zero).
    - Se o resto da divisão for maior ou igual a 2, então o dígito verificador é igual a 11 menos o resto da
    divisão (11 - resto).

No nosso exemplo temos que o resto é 8 então faremos 11-8 = 3. Logo o primeiro dígito verificador é 3. Então
sabemos que o CPF deve ser:  111.444.777-3X

Para  calcular o segundo dígito vamos usar o primeiro dígito já calculado. Vamos montar a mesma tabela de
multiplicação usada no cálculo do primeiro dígito. Só que desta vez usaremos na segunda linha os valores
11,10,9,8,7,6,5,4,3,2 já que estamos incluindo mais um dígito no cálculo:
	
Somamos: 11 + 10 + 9 + 32 + 28 + 24 + 35 + 28 + 21 + 6 = 204
Dividimos o total do somatório por 11 e consideramos o resto da divisão.
204 / 11  =  18  e  resto 6

Aplicamos a mesma regra que utilizamos para obter o primeiro dígito:
    - Se o resto da divisão for menor que 2, então o dígito é igual a 0 (Zero).
    - Se o resto da divisão for maior ou igual a 2, então o dígito é igual a 11 menos o resto da divisão
    (11 - resto).

11-6 = 5, logo 5 é o nosso segundo dígito verificador e o CPF completo é:
    111.444.777-35

O CPF de entrada deve ser considerado válido se os dígitos fornecidos pelo usuário forem os mesmos dígitos
calculados através do processo acima. '''

def valida_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        return "Inválido"

    def calcula_digito(numeros, multiplicador):
        total = sum(int(num) * mult for num, mult in zip(numeros, multiplicador))
        restante = total % 11
        return 0 if restante < 2 else 11 - restante

    nove_digitos = cpf[:9]
    primeiro_digito_mult = range(10, 1, -1)
    primeiro_digito = calcula_digito(nove_digitos, primeiro_digito_mult)

    dez_digitos = nove_digitos + str(primeiro_digito)
    segundo_digito_mult = range(11, 1, -1)
    segundo_digito = calcula_digito(dez_digitos, segundo_digito_mult)

    return "Válido" if cpf[9:] == f"{primeiro_digito}{segundo_digito}" else "Inválido"

cpf = input("Digite o CPF na forma XXX.XXX.XXX-XX: ")
validador = valida_cpf(cpf)
print(f"O CPF informado é: {validador}")