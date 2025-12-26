# 37.- Genera un programa que nos indique si es de noche, de día o de tarde según la hora proporcionada por el usuario.

from datetime import datetime

def comprobar_hora(hora_string):
    hora = datetime.strptime(hora_string, "%H:%M").hour
    if hora >= 6 and hora < 13:
        print(f"A las {hora_string} es de día.")
    elif hora >= 13 and hora < 21:
        print(f"A las {hora_string} es por la tarde.")
    else:
        print(f"A las {hora_string} es de noche.")

hora = input("Introduce una hora:")

comprobar_hora(hora)