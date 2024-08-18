'''Faça um programa que leia um número de celular e, caso o número tenha apenas 8 dígitos, acrescente o 9 na
frente. Caso o número já tenha 9 dígitos, verifique se o primeiro dígito é 9. Adicione o separador "-" na sua
impressão.'''

def formata_numero(num):
    # Remove caracteres não numéricos
    num = ''.join(filter(str.isdigit, num))
    
    #Valida número
    if len(num) == 8:
        num = '9' + num
    elif len(num) == 9:
        if num[0] != '9':
            return "Número inválido: deve começar com 9."
    
    # Adiciona o separador "-" no número
    if len(num) == 9:
        format_numero = num[:5] + '-' + num[5:]
        return format_numero
    else:
        return "Número inválido: deve ter 8 ou 9."

numero_celular = input("Digite o número do celular: ")

format_numero = formata_numero(numero_celular)
print(f"Número formatado: {format_numero}")
