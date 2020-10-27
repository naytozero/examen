print("digite el precio del articulo: ")
precio=int(input())
if precio <=0:
    print("no ahi descuento")
else:
    if precio <=100:
        print("el bono es de  10 % " ,precio * 0.10)
       
    else:
        if precio >=200:
            print("el  descuento r es 15 % " ,precio * 0.15)

        else:
             if precio >=100:
               print("el descuento  es 12 % " ,precio * 0.12)
       
print ("el total a pagar es ",precio-())  
           