num1 = None
num2 = None
menor = None
maior = None
while(not isinstance(num1, int) or num1 < 0 or not isinstance(num2, int) or num2 < 0):
    try:
        num1 = int(input("Insira o primeiro número: "))
        num2 = int(input("Insira o segundo número: "))
    except ValueError:
        print("Por favor, insira um número inteiro válido.")
        num1 = num2 = None
if num1 > num2:
    maior = num1
    menor = num2
else:
    maior = num2
    menor = num1
    
while menor <= maior:
    print(menor)
    menor += 1