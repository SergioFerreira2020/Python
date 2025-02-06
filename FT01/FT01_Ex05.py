import math

cateto_a = float(input("Insira o valor do cateto a: "))
cateto_b = float(input("Insira o valor do cateto b: "))

hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)
print(f"O valor da hipotenusa é: {hipotenusa}")