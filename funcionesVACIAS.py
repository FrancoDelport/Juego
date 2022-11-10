from configuracion import *
import random
import math

def quitar_salto(palabra):
    cadena=""
    for letra in palabra:
        if letra!="\n":
            cadena=cadena+letra
    return cadena

def nuevaPalabra(lista):
    palabra=random.choice(lista)
    return palabra

def lectura(archivo, salida, largo):
    lineas = archivo.readlines()
    for linea in lineas:
        cadena=quitar_salto(linea)
        if len(cadena) == largo:
         salida.append(cadena)
    print(salida)

def revision(palabraCorrecta, palabra, correctas, incorrectas, casi):
    cont=0
    if len(palabraCorrecta) != len(palabra):
        return False
    else:
        for i in range(len(palabraCorrecta)):
            if(palabraCorrecta[i] == palabra[i]):
                cont=cont+1
        if cont==len(palabraCorrecta):
            correctas.append(palabra)
            return True
        else:
            incorrectas.append(palabra)
            return False









