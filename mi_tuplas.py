print("Ejemplo de tuplas")
canciones = ("Te amo", "El noa noa", "Amor eterno")
print(canciones)
y = list(canciones)
y[1] = "La puerta negra"
x = tuple(y)
print(x)