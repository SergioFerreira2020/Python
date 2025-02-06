import math
num1 = None
num2 = None
num3 = None
num4 = None

while((not isinstance(num1, int) or num1 < 0) or (not isinstance(num2, int) or num2 < 0) or (not isinstance(num3, int) or num3 < 0) or (not isinstance(num4, int) or num4 < 0)):
    try:
        num1 = int(input("Insira o primeiro número: "))
        num2 = int(input("Insira o segundo número: "))
        num3 = int(input("Insira o terceiro número: "))
        num4 = int(input("Insira o quarto número: "))
    except ValueError:
        print("Por favor, insira um número inteiro válido.")
        num1 = num2 = num3 = num4 = None

media = math.ceil((num1 + num2 + num3 + num4) / 4)
print(f"A média dos números é: {media}")