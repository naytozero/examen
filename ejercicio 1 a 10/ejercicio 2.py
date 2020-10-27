s=int(input("ingrese cantidad hamburguesa Sencilla "))
d=int(input("ingrese cantidad hamburguesa Doble "))
t=int(input("ingrese cantidad hamburguesa Triples "))
Sencilla=20
Doble=25 
Triples=28
if s  <=0:
    print ("no ahi orden de hamburguesa Sencilla")
else:
    if s >=1:
         print("el costo es hamburguesa Sencilla " ,Sencilla*s )

if d <=0:
    print("no ahi orden de hamburguesa doble" )
else:
    if d >=1:
        print("el costo de la hamburguesa doble es " ,Doble*d )
if t <=0:
    print("no ahi orden de hamburguesa Triples "  )

else:
    if t >=1:
        print("el costo es hamburguesa Triples ",Triples*t )
pago = Sencilla*s + Doble*d + Triples*t 
print("el total a pagar es ",pago)