# coding=utf-8
import os
from tqdm import tqdm
# Directorio a almacenar el codigo
os.chdir('C:\\Users\\frahi\\PycharmProjects\\HotelesPI\\Codigos')
countTipoHab = 1  # IDHabitación, Modificar en caso solo requerir empezar de un ID más alto

tipo_habitacion = ["Habitacion Individual", "Habitacion doble de uso individual","Habitacion doble",
                   "Habitacion con cama supletoria","Habitacion triple","Junior Suites","Suites","Suite nupcial"]

archivoServicios = open("tipo_habitacion.sql", "w")
archivoServicios.write("INSERT INTO `hotelera`.`tipohabitaciones` (`id`,`descripcion`) \nVALUES \n")
for th in tipo_habitacion:
    archivoServicios.write("(" + str(tipo_habitacion.index(th))+", \"" + th+"\"),\n")
