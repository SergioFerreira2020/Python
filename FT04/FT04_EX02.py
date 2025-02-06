estado = None
while(estado != "s" and estado != "S" and estado != "c" and estado != "C" and estado != "v" and estado != "V"):
    estado = input("Insira o estado civil: ")

match estado:
    case "s" | "S":
        print("Estado Civil : Solteiro")
    case "c" | "C":
        print("Estado Civil : Casado")
    case "v" | "V":
        print("Estado Civil : Viúvo")
    case _:
        print("Estado Civil Inválido")