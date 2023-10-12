from random import choice

departamento = {"antioquia":"medellin", "bucaramanga": "bogota", "cauca":"cauca"}

for clave, valor in departamento.items():
    print(f"{clave}:{valor}")

while True:
    i = 0
    print(" 1-ingresar ciudad \n 2-salir")
    op = input("ingrese opcion: ")
    if op == "1":
     print("Departamento aleatorio: ")
     aleatorio = choice(list(departamento.values()))
     print(aleatorio)
     ciudad = input("ingrese ciudad: ")
     while ciudad != aleatorio:
         ciudad = input("ingrese ciudad que coincida: ")
         i+=1
         if ciudad == aleatorio and i <= 3:
             print("ciudad correcta!")
             break
         else:
             print("hasta luego")
             break
    if op == "2": 
        break   
         
            
     
        
            
        
            
                 
        
            
         
        
     
         
     
             
        
         
        
      
    
     
    