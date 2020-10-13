print("ingrese calificaciones deel alumno:")
primera =float(input("primera nota"))
segunda =float(input("segunda nota"))
tercera =float(input("tercera nota"))
cuarta = float(input("cuarta nota"))
primera*=0.10
segunda*=0.15
tercera*=0.25
cuarta  *=0.50
final=primera+segunda+tercera+cuarta
print(f"Esta es la calificacion del alumno:{final:.2f}")