hora = int(input("Insira as horas: "))
minutos = int(input("Insira os minutos: "))
segundos = int(input("Insira os segundos: "))
output = "{} hora(s), {} minuto(s) e {} segundo(s)" .format(hora,minutos,segundos)
segundos += (minutos + (hora * 60)) * 60 
output += " são {} segundos" .format(segundos)
print(output)