
#ingresar el texto 
texto = input("Introduce un texto: ")

#que caracter quiero cambiar
letra_reemplazar = input("Introduce la letra que deseas reemplazar: ")


def leer_diccionario(**kwargs):
    with open("dicc.txt", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    for i, linea in enumerate(lineas, 1):
        print(f"Línea {i}: {linea.strip()}") 

leer_diccionario()


posicion = int(input("Ingresar la posicion para hacer el cambio: "))
contador = 0

#print(posicion)
contenido = None


with open('dicc.txt', 'r', encoding="utf-8") as archivo:
    lineas = archivo.readlines()
    # Verificar si el número está dentro del rango de líneas
    if 1 <= posicion <= len(lineas):
        
        contenido = lineas[posicion - 1].strip()
    else:
        print("El número está fuera del rango de líneas del archivo.")



texto_modificado = texto.replace(letra_reemplazar, contenido)
            
print("texto inicial: " +texto)
print("text con caracter unicode: "+texto_modificado)

