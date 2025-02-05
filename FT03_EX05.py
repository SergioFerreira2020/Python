n = None
while not isinstance(n, (int, float)):
    try:
        n = input('Digite um número inteiro e positivo: ')
        if '.' in n:
            n = float(n)
        else:
            n = int(n)
    except ValueError:
        print('Por favor, insira um número válido.')
if n > 0:
    print('O número é positivo.')
elif n < 0:
    print('O número é negativo.')
else:
    print('O número é zero.')