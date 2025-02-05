num1 = None
num2 = None
while not isinstance(num1, float) or not isinstance(num2, float):
    try:
        num1 = float(input("Inserir o primeiro float: "))
        num2 = float(input("Inserir o segundo float: "))
    except ValueError:
        print("Valor inválido. Tente novamente.")
        
if num1 > num2:
    print(f"{num1} é maior que {num2}")
elif num1 < num2:
    print(f"{num1} é menor que {num2}")
else:
    print(f"{num1} é igual a {num2}")