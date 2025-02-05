print("Escolha a operaçao desejada:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
op = None
num1 = None
num2 = None
while op not in [1, 2, 3, 4]:
    try:
        op = int(input("Insira a opção desejada: "))
    except ValueError:
        print("Por favor, insira um número válido.")
while not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
    try:
        num1 = input("Insira o primeiro número: ")
        num2 = input("Insira o segundo número: ")
        if "." in num1:
            num1 = float(num1)
        else:
            num1 = int(num1)
        if "." in num2:
            num2 = float(num2)
        else:
            num2 = int(num2)
    except ValueError:
        print("Por favor, insira um número válido.")
        
if op == 1:
    print("O resultado da soma é: ", num1 + num2)
elif op == 2:
    print("O resultado da subtração é: ", num1 - num2)
elif op == 3:
    print("O resultado da multiplicação é: ", num1 * num2)
else:
    print("O resultado da divisão é: ", num1 / num2)