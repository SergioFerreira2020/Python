months = [
    "Janeiro",   
    "Fevereiro", 
    "Março",     
    "Abril",     
    "Maio",      
    "Junho",    
    "Julho",     
    "Agosto",    
    "Setembro",  
    "Outubro",   
    "Novembro", 
    "Dezembro"   
]
month_number = None
while not isinstance(month_number, int) or month_number < 1 or month_number > 12:
    try:
        month_number = int(input("Introduza o número do mês (1-12): "))
    except ValueError:
        print("Entrada inválida! Por favor, insira um número inteiro.")
        month_number = None

print(f"O mês é: {months[month_number - 1]}")

# Switch statement     
match month_number:
    case 1:
        print("Janeiro")
    case 2:
        print("Fevereiro")
    case 3:
        print("Março")
    case 4:
        print("Abril")
    case 5:
        print("Maio")
    case 6:
        print("Junho")
    case 7:
        print("Julho")
    case 8:
        print("Agosto")
    case 9:
        print("Setembro")
    case 10:
        print("Outubro")
    case 11:
        print("Novembro")
    case 12:
        print("Dezembro")
    case _:
        print("Mês inválido")