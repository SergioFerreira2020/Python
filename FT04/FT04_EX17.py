num = None
soma = 0
media = 0
i = 1
while i < 20 : 
    while not isinstance(num, float):
        num = float(input('Insira um número real: '))
        if not isinstance(num, float):
            print('Insira um número real válido.')
            num = None
    i += 1
    soma += num
print(f'A soma dos números é: {soma} e a média é: {soma/20}')