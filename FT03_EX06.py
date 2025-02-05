num1 = None
num2 = None
num3 = None
while not isinstance(num1, float) and not isinstance(num2, float)and not isinstance(num3, float):
    try:
        num1 = float(input("Inserir o primeiro float: "))
        num2 = float(input("Inserir o segundo float: "))
        num3 = float(input("Inserir o terceiro float: "))
    except ValueError:
        print("Valor inválido. Tente novamente.")
        
if num1 > num2 and num1 > num3:
    print(f"{num1} é maior que {num2} e {num3}")
elif num2 > num1 and num2 > num3:
    print(f"{num2} é maior que {num1} e {num3}")
elif num3 > num1 and num3 > num2:
    print(f"{num3} é maior que {num1} e {num2}")
else:
    print(f"{num1}, {num2} e {num3} são iguais")