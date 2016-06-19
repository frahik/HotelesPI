# coding=utf-8
import os
from tqdm import tqdm
# Directorio a almacenar el codigo
os.chdir('C:\\Users\\frahi\\PycharmProjects\\HotelesPI\\Codigos')
countserv = 1  # IDHabitación, Modificar en caso solo requerir empezar de un ID más alto

#  Servicios que incluye cada habitación
servicios = ["Aire acondicionado", "Servicio al cuarto", "Television por cable", "Jacuzzi",
           "Vista al exterior", "Caja de seguridad", "Antiruido", "Wi-Fi"]

archivoServicios = open("Servicio.sql", "w")
archivoServicios.write("INSERT INTO `hotelera`.`servicios` (`idservicio`,`serviciouno`,`serviciodos`, `serviciotres`) \nVALUES \n")

for i in tqdm(servicios):
    for j in servicios[servicios.index(i)+1:]:
        for k in servicios[servicios.index(j)+1:]:
            archivoServicios.write("(" + str(countserv) + ",\"" + '\", \"'.join((i,j,k))+"\"),\n")
            countserv+=1
archivoServicios.close()