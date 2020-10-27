import random

def cantidadNumCeroMenorCeroMayorCero():
    blanco, verde, rojo=0,0,0
    Cantidad=int(input("Ingrese la cantidad de focos:"))
    
    for caja in range(1,Cantidad+1):
        focos = random.randrange(-1000, 1000)

        print(f"posicion {caja}: {focos}")
        
        if focos==0:
            verde=verde+1
        elif focos>0:
            blanco=blanco+1
        else:
            rojo=rojo+1
   
    print(f"La cantidad de focos blancos  es: {blanco}")
    print(f"La cantidad de focos verdes es: {verde}")
    print(f"La cantidad de focos rojos es: {rojo}")

cantidadNumCeroMenorCeroMayorCero()