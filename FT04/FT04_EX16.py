num = None
while not isinstance(num, int) or (num < 0 or num > 10):
    try:
        num = int(input('Insira um numero entre 0 a 10: '))
        if num < 0 or num > 10:
            print('Número fora do intervalo permitido. Insira um número inteiro válido entre 0 a 10..')
        else:
            print(f'O número {num} está dentro do intervalo permitido.')
    except ValueError:
        print('Por favor, insira um número inteiro válido entre 0 a 10.')
        

