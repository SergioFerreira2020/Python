num = None
while not isinstance(num, int):
    try:
        num = int(input("insira um inteiro: "))
    except ValueError:
        print("Por favor, insira um número válido.")
if num % 2 == 0:
    print("O número", num, "é par")
else:
    print("O número", num, "é ímpar")