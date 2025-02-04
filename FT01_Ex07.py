km = int (input("Insira os kilometros: "))
litros = int(input("Insira a quantidade de litros consumidos: "))
consumo = km / litros

if consumo >= 14:
    print("Consumo de" ,consumo, "km/l, Venda o carro!")
elif 8 <= consumo < 14:
    print("Consumo de" ,consumo, "km/l, Econômico!")
else:
    print("Consumo de" ,consumo, "km/l, Super econômico!")