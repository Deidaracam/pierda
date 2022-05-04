import random


aleatorio = random.randrange(0, 3)
elijePc = ""
print("1)Piedra")
print("2)Papel")
print("3)Tijera")
opcion = int(input("Que elijes: "))

if opcion == 1:
    elijeUsuario = "piedra"
elif opcion == 2:
    elijeUsuario = "papel"
elif opcion == 3:
    elijeUsuario = "tijera"
print("Tu elijes: ", elijeUsuario)

if aleatorio == 0:
    elijePc = "piedra"
elif aleatorio == 1:
    elijePc = "papel"
elif aleatorio == 2:
    elijePc = "tijera"
print("PC elijio: ", elijePc)
print("...")
if elijePc == "piedra" and elijeUsuario == "papel":
    print("Ganaste que pro, papel envulve piedra")
elif elijePc == "papel" and elijeUsuario == "tijera":
    print("Ganaste que pro, Tijera corta papel")
elif elijePc == "tijera" and elijeUsuario == "piedra":
    print("Ganaste que pro, Piedra pisa tijera")
if elijePc == "papel" and elijeUsuario == "piedra":
    print("perdiste por manco , papel envulve piedra")
elif elijePc == "tijera" and elijeUsuario == "papel":
    print("perdiste por manco , Tijera corta papel")
elif elijePc == "piedra" and elijeUsuario == "tijera":
    print("perdiste por manco, Piedra pisa tijera")
elif elijePc == elijeUsuario:
    print("empate por gey")