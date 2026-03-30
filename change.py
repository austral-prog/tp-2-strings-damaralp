def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """

    gasto= 23.75
    Dinero_recibido= 100
    pesos=76
    vuelto=Dinero_recibido-gasto
    centavos= int(round((vuelto-pesos)*100))
    print(f"Ingresar gasto:\n{gasto}")
    print(f"Dinero recibido\n{Dinero_recibido}")
    print(f"\nVuelto\n")
    print(f"Pesos:\n{int(pesos)}")
    print(f"Centavos:\n{centavos}")
change()
