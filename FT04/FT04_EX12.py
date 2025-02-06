num = None
i = 1
fatorial = 1
while not isinstance(num, int):
    try:
        num = int(input("Insira um número inteiro: "))
    except ValueError:
        print("Insira um número inteiro válido.")

while i <= num:
    fatorial *= i
    i += 1
    
print(f"O fatorial de {num} é: {fatorial}")