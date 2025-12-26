# 40.- Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe:
#     a. Solicitar al usuario el precio original de un artículo.
#     b. Preguntar si tiene un cupón de descuento (respuesta sí o no).
#     c. Si la respuesta es sí, solicitar el valor del cupón de descuento.
#     d. Aplicar el descuento al precio original, siempre que el valor del cupón sea válido (mayor a cero).
#     e. Mostrar el precio final de la compra, considerando o no el descuento.
#     f. Usar estructuras de control de flujo (if, elif, else) para llevar a cabo las acciones.

def calcular_descuento(precio_original, tipo_descuento, valor_descuento):
    if tipo_descuento == "€":
        if valor_descuento <=0:
            return "Descuento no válido."
        elif valor_descuento >= precio_original:
            return "El precio final es de 0€."
        else:
            return f"El precio final es de {precio_original - valor_descuento}€."
    elif tipo_descuento == "%":
        if valor_descuento <=0:
            return "Descuento no válido."
        elif valor_descuento >= 100:
            return "El precio final es de 0€."
        else:
            return f"El precio final es de {precio_original * valor_descuento / 100}€."
    else:
        return "Tipo de descuento no válido."
    
precio_original = float(input("Escribe el precio original del producto:"))
tipo_descuento = input('''Escribe el símbolo del tipo de descuento que tienes:
"€" si tienes un descuento al total
"%" si tienes un descuento de porcentaje''')
valor_descuento = float(input("Escribe el valor del descuento:"))

print(calcular_descuento(precio_original, tipo_descuento, valor_descuento))