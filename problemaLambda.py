from random import choice

opciones = ["papel", "piedra", "tijera"]
juego = lambda: choice(list(opciones))

resultados = {
    ("piedra", "papel"): "gana maquina",
    ("piedra", "tijera"): "gana jugador",
    ("piedra", "piedra"): "empate",
    ("papel", "tijera"): "gana maquina",
    ("papel", "piedra"): "gana jugador",
    ("papel", "papel"): "empate",
    ("tijera", "piedra"): "gana maquina",
    ("tijera", "papel"): "gana jugador",
    ("tijera", "tijera"): "empate",
}

while True:
    print("¿Desea jugar? (si/no)")
    op = input("Ingrese opción: ")

    if op.lower() != "si":        
        break

    opc = input("Ingrese piedra, papel o tijera: ").lower()
    aleatorio = juego()
        
    while opc != "piedra" and opc != "papel" and opc != "tijera":
     opc = input("Opción no válida. Por favor, elija piedra, papel o tijera.")
    if (opc, aleatorio) in resultados:
     resultado = resultados[(opc, aleatorio)]
     print(f'Jugador saca {opc}, máquina saca {aleatorio}. Resultado: {resultado}')
     
            
        
                                