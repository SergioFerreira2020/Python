N = None
i = 1
s = 0
while(not isinstance(N, int) or N < 0):
    try:
        N = int(input("Insira um número inteiro positivo: "))
    except ValueError:
        print("Por favor, insira um número inteiro válido.")
        N = None
while i<=N:
    s+=i
    i+=1
print(f"A soma dos números da sequência é: {s}")