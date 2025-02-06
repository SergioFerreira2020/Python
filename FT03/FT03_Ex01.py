num = None
while not isinstance(num, int):
    try:
        num = int(input("insira um inteiro: "))
    except ValueError:
        print("Por favor, insira um número válido.")
if num > 20:
    print(num/2)