import math
pi = math.pi
r = None
while not isinstance(r, float):
    try:
        r = float(input("Insira o raio: "))
    except ValueError:
        print("Por favor, insira um número válido.")
volume = round( 4/3 * pi * r**3, 2)
print("Volume da esfera: ", volume)