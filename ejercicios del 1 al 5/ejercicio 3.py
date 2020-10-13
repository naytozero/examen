#vacuna para el covid
print("digite la edad de la persona:")
edadpersona=int(input())
if edadpersona<=0:
    print("edad incorrecta ¿error al digitar la edad")
else:
    if edadpersona>=70:
        print("se le aplicara la vacuna de tipo c")
    else:
        if edadpersona>=16:
            print("se le aplicara la vacuna de tipo B")

        else:
            print("Se le aplicara la vacuna de tipo A")
