print("escriba los puntos del profesor: ")
puntos=int(input())
if puntos <=0:
    print("no ahi puntos")
else:
    if puntos <=100:
        print("el bono es de  10%",puntos)
    else:
        if puntos <=150:
            print("el bono del profesor es 50%",puntos)

        else:
             if puntos >=151:
                print("el bono del profesor es 80%" ,puntos)
