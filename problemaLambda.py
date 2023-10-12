from random import choice


juego = lambda: print(choice("papel", "piedra", "tijera"))

while True: 
    print("desea jugar s\n ")
    op = input("ingrese opcion: ")
    if op == "s":
        opc = input("ingrese piedra papel o tijera: ")
        if opc != "piedra" or "papel" or "tijera":
            print("opcion invalida")
        
                                