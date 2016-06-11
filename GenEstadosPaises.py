import os

# Directorio a almacenar el codigo
os.chdir('C:\\Users\\Ucol\\PycharmProjects\\PIHoteles\\Codigos')

pais = ["Mexico",
        "Austria", "Suiza", "Nevada", "Emiratos Arabes Unidos",
        "Estados Unidos"]

Estados = ["Aguascalientes, Mexico",
           "Baja California, Mexico", "Baja California Sur, Mexico", "Campeche, Mexico",
           "Chiapas, Mexico", "Chihuahua, Mexico", "Ciudad de Mexico, Mexico", "Coahuila de Zaragoza, Mexico",
           "Colima, Mexico", "Durango, Mexico", "Guanajuato, Mexico", "Guerrero, Mexico", "Hidalgo, Mexico",
           "Jalisco, Mexico",
           "Mexico, Mexico", "Michoacan de Ocampo, Mexico", "Morelos, Mexico", "Nayarit, Mexico", "Nuevo Leon, Mexico",
           "Oaxaca, Mexico", "Puebla, Mexico", "Queretaro, Mexico", "Quintana Roo, Mexico", "San Luis Potosi, Mexico",
           "Sinaloa, Mexico", "Sonora, Mexico", "Tabasco, Mexico", "Tamaulipas, Mexico", "Tlaxcala, Mexico",
           "Veracruz, Mexico", "Yucatan, Mexico", "Zacatecas, Mexico", "Viena, " + str(pais[1]),
           "Zurich, " + str(pais[2]), "Las vegas, " + str(pais[3]), "Dubai, " + str(pais[4]),
           "Alabama, " + str(pais[5]), "Alaska, " + str(pais[5]), "Arizona, " + str(pais[5]),
           "Arkansas, " + str(pais[5]),
           "California, " + str(pais[5]), "Colorado, " + str(pais[5]), "Dakota del Norte, " + str(pais[5]),
           "Dakota del sur, " + str(pais[5]),
           "Delaware, " + str(pais[5]), "Florida, " + str(pais[5]), "Georgia, " + str(pais[5]),
           "Hawai, " + str(pais[5]), "Idaho, " + str(pais[5]),
           "Illinois, " + str(pais[5]), "Indiana, " + str(pais[5]), "Iowa, " + str(pais[5]), "Kansas, " + str(pais[5]),
           "Kentucky, " + str(pais[5]),
           "Luisiana, " + str(pais[5]), "Maine, " + str(pais[5]), "Maryland, " + str(pais[5]),
           "Massachusetts, " + str(pais[5]),
           "Michigan, " + str(pais[5]), "Minnesota, " + str(pais[5]), "Misisipi, " + str(pais[5]),
           "Misuri, " + str(pais[5]),
           "Montana, " + str(pais[5]), "Nebraska, " + str(pais[5]), "Nevada, " + str(pais[5]),
           "Nueva York, " + str(pais[5]),
           "Nuevo Mexico, " + str(pais[5]), "Ohio, " + str(pais[5]), "Oklahoma, " + str(pais[5]),
           "Oregon, " + str(pais[5])]

archivoEstados = open("Estados.sql", "w")
archivoPaises = open("Pais.sql", "w")
archivoEstados.write("INSERT INTO `hotelera`.`ciudades` (`idestado`,`nombre`,`idpais`) \nVALUES \n")
archivoPaises.write("INSERT INTO `hotelera`.`paises`  (`idpais`, `nombre`) \nVALUES \n")

for ciudad in range(len(Estados)):
    idpais = pais.index(str(Estados[ciudad]).split(", ")[1])
    archivoEstados.write(
        "(" + str(ciudad + 1) + ", \'" + str(Estados[ciudad]).split(", ")[0] + "\' ," + str(idpais + 1) + "),\n")
    archivoPaises.write("(" + str(idpais + 1) + ", \'" + str(pais[idpais]) + "\' ), \n")
archivoEstados.write(";")
archivoPaises.write(";")


# Pequeña función para enviar la lista de estados
def recuperarEstado():
    return Estados
