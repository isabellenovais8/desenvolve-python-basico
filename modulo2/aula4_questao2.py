'''
2) Leia um valor inteiro correspondente a uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
Fórmula de conversão: C = (F - 32) * (5/9), sendo C o valor em graus Celsius e F o valor em Fahrenheit.
Antes de imprimir, converta o valor em Celsius para inteiro. A mensagem deve estar formatada da seguinte maneira:

86 graus Fahrenheit são 30 graus Celsius.
'''

temp_fah = int(input("Informe a temperatura em Fahrenheit: "))
temp_cels = (temp_fah - 32) * (5/9)

print(f"{temp_fah} graus Fahrenheit são {temp_cels:2.0f} graus Celsius.")