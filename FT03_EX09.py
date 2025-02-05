nome = input("Insira o seu nome: ")
idade = None 
peso = None
altura = None
while not isinstance(idade,int) or not isinstance(peso,float) or not isinstance(altura,float):
    try:
        idade = int(input("Insira a sua idade: "))
        peso = float(input("Insira o seu peso: "))
        altura = float(input("Insira a sua altura: "))
    except ValueError:
        print("Por favor, insira valores válidos.")

IMC = peso / (altura ** 2)

if IMC < 17:
    print("Muito abaixo do peso ideal.")
elif IMC >= 17 and IMC < 18.5:
    print("Abaixo do peso.")
elif IMC >= 18.5 and IMC < 25:
    print("Peso normal.")
elif IMC >= 25 and IMC < 30:
    print("Acima do peso.")
elif IMC >= 30 and IMC < 35:
    print("Obesidade I.")
elif IMC >= 35 and IMC < 40:
    print("Obesidade II (severa).")
else:
    print("Obesidade III (mórbida).")