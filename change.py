def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """

    gasto = float(input())
    recibido = int(input())
 
    vuelto = round(recibido - gasto, 2)
    pesos = int(vuelto)
    centavos = round((vuelto - pesos) * 100)
 
    print("Ingresar gasto:")
    print(gasto)
    print("Dinero recibido")
    print(recibido)
    print()
    print("Vuelto")
    print()
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)
 
