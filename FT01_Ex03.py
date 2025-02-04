val = None
while not isinstance(val, int):
    try:
        val = int(input("insira um inteiro: "))
    except ValueError:
        print("Por favor, insira um número válido.")
double = val * 2
output = "O dobro de {} é {}".format(val,double)

print ("O dobro de", val, "é" , double)
print (output)