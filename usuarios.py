cuantos = int(input("Cuantos usuarios va a crear?"))

usuarios = []
for i in range(cuantos):
    nombre = input("Inserte el nombre del usuario:")
    usuarios.append(nombre)
print(usuarios)