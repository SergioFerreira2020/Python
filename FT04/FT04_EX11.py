num = None 
i = 1
soma = 0
multiplicacao = 1
while not isinstance(num, int) or num < 0:
    try:
        num = int(input("Insira um número inteiro positivo: "))
    except ValueError:
        print("Por favor, insira um número inteiro válido.")
        num = None
while i <= num:
    soma += i
    multiplicacao *= i
    i += 1
print(f"A soma dos números da sequência é: {soma}")
print(f"A multiplicação dos números da sequência é: {multiplicacao}")