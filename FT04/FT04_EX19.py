num = None
i = 1
while not isinstance(num, int) or num < 1:
    try:
        num = int(input("Insira um número inteiro: "))
    except ValueError:
        print("Digite um número inteiro válido.")

num2 = num
while i <= num:
    print(f"{i}     {num2}")
    num2 -= 1
    i += 1