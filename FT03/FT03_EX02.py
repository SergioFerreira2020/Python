num1 = None
num2 = None
while not isinstance(num1, int) and not isinstance(num2, int):
    try:
        num1 = int(input("Insira o primeiro número: "))
        num2 = int(input("Insira o segundo número: "))
    except ValueError:
        print("Por favor, insira um número válido.")
if num1 != num2:
    print("Os números são diferentes")
else:
    print("Os números são iguais")