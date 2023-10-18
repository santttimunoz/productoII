from random import choice

departamento = {"antioquia":"medellin", "bucaramanga": "bogota", "cauca":"popayan"}

#for clave, valor in departamento.items():
#   print(f"{clave}:{valor}")

while True:
    i = 0
    print(" desea adivinar la ciudad? \n 1-ingresar ciudad \n 2-salir")
    op = input("ingrese opcion: ")
    if op == "1":
     aleatorio = choice(list(departamento.keys()))
     print(f"Departamento aleatorio: {aleatorio}")     
     ciudad = departamento[aleatorio]
     i = 0                        
     while True:
      departamento = input("ingrese la ciudad del departamento: ")                 
      if departamento == ciudad:
       print("ciudad correcta!")
       break
      else:
       i+=1
       if i < 3:
        print("fallaste, intena otra vez")        
       else:
        print("fallaste 3 veces, hasta luego")
        break
    if op == "2": 
        break   
         
            
     
        
            
        
            
                 
        
            
         
        
     
         
     
             
        
         
        
      
    
     
    