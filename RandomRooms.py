# coding=utf-8
# Modulos
import random
import os
from tqdm import tqdm

# Directorio a almacenar el codigo
os.chdir('C:\\Users\\frahi\\PycharmProjects\\HotelesPI\\Codigos')

counthabit = 1  # IDHabitación, Modificar en caso solo requerir empezar de un ID más alto

archivo = open("Hoteles.txt", "r")
habitacion = open("Habitacion.txt", "w")
servicios = open("Servicio.sql","r").readlines()

# Descripciones de las habitaciones
tipo_habitacion = ["Habitacion Individual: Ideal para quienes viajan solos;",
                   "Habitacion doble de uso individual: Para quienes viajan solos y requieren mas espacio;",
                   "Habitacion doble: Como su nombre lo indica, esta clase de habitaciones son para dos personas. Las camas varian, pueden ser matrimoniales o dos camas individuales independientes;",
                   "Habitacion con cama supletoria: Estas habitaciones son ideales para quienes viajan con algun menor de edad;",
                   "Habitacion triple: Simple: estas habitaciones cuentan con 3 camas, o 2 mas una supletoria. Es perfecta para los viajes con tus amigos;",
                   "Junior Suites: cuentan con habitacion doble, bano y salon;",
                   "Suites: Conocidas por ser las mejores y mas lujosas habitaciones en cualquier hotel, cuentan con dos habitaciones dobles, 2 banos, salon y estancia;",
                   "Suite nupcial: Pensada para aquellas parejas recien casadas y que quieren disfrutar de una luna de miel con privacidad e intimidad;"]

# Calidad de la habitación
estadohabit = ["Bueno", "Regular", "Excelente"]

for lines in archivo.readlines():
    hotelid = lines.split("(")[1].split(",")[0]

    # Genera una Habitación de manera pseudoaleatoria
    piso = random.randint(1, 5)  # Genera un Piso de manera PseudoAleatoria; No es necesario modificar.

    # Genera 5 Habitaciones por cada hotel
    for habit in range(5):
        seleccion = str(random.sample(servicios, 1))
        deschabitacion = str(random.sample(tipo_habitacion, 1)).split("['")[1].split("']")[0]  # Selecciona una descripcion Pseudo-Aleatoria de la lista habitaciones.
        lista = []
        lista.append(seleccion.split("\"")[1])
        lista.append(seleccion.split("\"")[3])
        lista.append(seleccion.split("\"")[5])

        descripciones = deschabitacion + " Incluye " + lista[0] + ", " + lista[1] + " y " + lista[2] + "."  # Crea una frase de descripcion usando los dos anteriores.
        if "Suite" in deschabitacion.split(":")[
            0]:  # Genera de manera "PseudoInteligente" un precio Pseudo-Aleatorio para las habitaciones.
            precio = random.randrange(1400, 2000, 9)
        else:
            precio = random.randrange(200, 1600, 9)

        # Escribe en el archivo en formato «(idhabitacion,numero_habitacion, piso, descripcion, precio, calidad/estado_habitacion, tipo_habitacion, idhotel, servicios),»
        #habitacion.write\
        print("(" + str(counthabit) + ",\"" + '\", \"'.join((str(piso * 10 + habit + 1), str(piso),
                        descripciones, str(precio), str(random.choice(estadohabit)), str(tipo_habitacion.index(deschabitacion.split(";")[0]+";")+1),
                        str(hotelid), seleccion.split("(")[1].split(",")[0] ))+"\"),\n")
        counthabit += 1
habitacion.close()
