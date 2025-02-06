taboada = None
i = 1
while(not isinstance(taboada, int) or taboada < 0):
    try:
        taboada = int(input("Insira um número inteiro positivo: "))
    except ValueError:
        print("Por favor, insira um número inteiro válido.")
        taboada = None
while i <= 10:
    print(f"{taboada} x {i} = {taboada*i}")
    i += 1
 