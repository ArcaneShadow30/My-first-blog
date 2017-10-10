import sys
from select import select
import math
import random

juego = True

while juego is True:
    def invalido():
        print("Respuesta invalida")

    print("1. iniciar test\n2.cerrar")
    respuesta = input()
    if respuesta == "2":
        juego = False
    if respuesta == "1":

        vidas = 3
        n = 1


        def vervidas():
            print("vidas: " + str(vidas))


        def incorrecto():
            print("incorrecto")
            if vidas == 0:
                print("perdiste")


        while vidas != 0:
            if n == 1:
                vervidas()
                print("1.Que haces aqui?\na.Jugar\nb.Quemando a un estudiante\nc.Define estar.\nd.Rosalia me obliga.")
                res1 = input()

                if res1 == "d":
                    n += 1
                else:
                    vidas -= 1
                    incorrecto()

            if n == 2:
                lista = ["cara", "cruz"]
                moneda = random.choice(lista)

                vervidas()
                print("2. Voy a lanzar una moneda, a que le apuestas? ")
                res2 = str(input("Escribe cara o cruz: "))

                if res2 == moneda:
                    n += 1
                elif res2 != moneda:
                    vidas -= 1
                    incorrecto()
                else:
                    print("respuesta invalida")

            if n == 3:
                r = random.randint(1, 10)
                h = random.randint(1, 10)
                AL = 2 * math.pi * r * h
                AB = math.pi * (r ** 2)
                AT = AL + 2 * AB
                ran1 = (2 * math.pi * random.randint(1, 10) * random.randint(1, 10)) + (
                2 * math.pi * (random.randint(1, 10) ** 2))
                ran2 = (2 * math.pi * random.randint(1, 10) * random.randint(1, 10)) + (
                2 * math.pi * (random.randint(1, 10) ** 2))
                ran3 = (2 * math.pi * random.randint(1, 10) * random.randint(1, 10)) + (
                2 * math.pi * (random.randint(1, 10) ** 2))

                vervidas()
                print("3. cual es el area de un cilindro de radio " + str(r) + " y altura " + str(h) + "?")
                print("a." + str(ran1) + "\nb." + str(ran2) + "\nc." + str(AT) + "\nd." + str(ran3))
                res3 = input()

                if res3 == "c":
                    n += 1
                elif res3 == "a" or "b" or "d":
                    vidas -= 1
                    incorrecto()
                else:
                    print("in")

            if n == 4:

                print("4. la siguiente pregunta expira a los 10 segundos, si no lo haces tus vidas se volverán cero")
                input("escribe ok para comenzar: ")


                vervidas()
                print("En que año fue la revolución francesa?\na.1788\nb.1789\nc.1799\nd.1787")
                select([sys.stdin], [], [], 10)
                res4 = input()

                if res4 == "b":
                    n += 1
                else:
                    vidas = 0
                    incorrecto()

            if n == 5:
                lista = list(range(0, 70, 7))
                vervidas()
                print("5. Cual es el siguiente numero en la sucesion: " + str(lista[:-1]))
                res5 = input()
                if int(res5) == lista[9]:
                    n +=1
                else:
                    vidas -= 1
                    incorrecto()

            if n == 6:
                vervidas()
                print(
                    "6. Qiin discibri imiriqui?\na.Cristibil Cilin.\nb.Simiil Liciini.\nc.Esto es estupido.\nd.Ti mimi.")
                res6 = input()
                if res6 == "a":
                    n += 1
                else:
                    vidas -= 1
                    incorrecto()

            if n == 7:
                palabras = []
                k = 0
                while k != 10:
                    nuevo = input("introduzca una palabra: ")
                    palabras.append(nuevo)
                    k += 1
                print("usted va a tener 5 segundos para responder lo siguiente, escriba ok cuando este listo.")
                input()
                vervidas()
                print("7.Cual fue la primera palabra que introdujo?")
                select([sys.stdin], [], [], 5)
                res7 = input()
                if res7 == palabras[0]:
                    n += 1
                else:
                    vidas -= 1
                    incorrecto()
            if n == 8:
               vervidas()
               print("8.mire las siguientes secuencias\n"
                     "A = 8 2 4 : 10\nB = 3 3 2: 2\nC = 12 5  1:?\n"
                     "cual es la solucion de la sucesion C?\n"
                     "a.18\nb.-18\nc.19\nd.8")
               res8 = input()
               if res8 == "d":
                    n += 1
               else:
                   vidas -= 1
                   incorrecto()

            if n == 9:
                vervidas()
                print("9.Has llegado muy lejos, mira que te regalo una vida.\na.ok \nb.no la quiero")
                res9 =input()
                if res9 == "a":
                    vidas += 1
                    n +=1
                else:
                    print("Que te dije que te la doy")
                    vidas += 1
                    n += 1
            if n == 10:
                vervidas()
                print("10. Cuanto me va a dar Samuel en programacion 1?\na.A\nb.A\nc.A\nd.A")
                res10 = input()
                if res10 == "a"or "b"or"c"or"d":
                    print("Has ganado")
                    break
                else:
                    vidas -= 1
                    incorrecto()
    else:
        invalido()