ano = None
while not isinstance(ano, int) :
    try:
        ano = int(input('Digite um ano: '))
    except ValueError:
        print('Por favor, insira um ano válido.')
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print('O ano', ano, 'é bissexto.')
else:
    print('O ano', ano, 'não é bissexto.')