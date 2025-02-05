lado1=None
lado2=None
lado3=None
while not isinstance(lado1,(int,float) or not isinstance(lado2,(int,float)) or not isinstance(lado3,(int,float))):
    try:
        lado1 = input("Insira o primeiro lado: ")
        lado2 = input("Insira o segundo lado: ")
        lado3 = input("Insira o terceiro lado: ")
        if "." in lado1:
            lado1 = float(lado1)
        else:
            lado1 = int(lado1)
        if "." in lado2:
            lado2 = float(lado2)
        else:
            lado2 = int(lado2)
        if "." in lado3:
            lado3 = float(lado3)
        else:
            lado3 = int(lado3)
    except ValueError:
        print("Por favor, insira um número válido.")
        
if lado1 == lado2 and lado1 == lado3:
    print("O triângulo é equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("O triângulo é isósceles.")
else:
    print("O triângulo é escaleno.")