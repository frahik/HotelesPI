from googleplaces import GooglePlaces, types, lang  # DOC GOOGLEPLACES https://github.com/slimkrazy/python-google-places
import os
from GenEstadosPaises import recuperarEstado  # DOC GenEstadosPaises NULL
from tqdm import trange  # DOC tqdm https://github.com/tqdm/tqdm

Estados = recuperarEstado()  # Recupera los estados
print "Ciudades Recuperadas: " + str(len(Estados))

print "Recuperando Hoteles: "

os.chdir('C:\\Users\\Ucol\\PycharmProjects\\PIHoteles\\Codigos')

# API_KEYS DE GOOGLEPLACES API
YOUR_API_KEY = 'AIzaSyAssfkvPlQ7uBLbXZSHVW5kJZNWdwre7Is'
google_places = GooglePlaces(YOUR_API_KEY)

try:
    log = open("log.log", "r")
    flag = int(str(log.readline()).split(":")[1].split("\\n")[0])
    count = int(str(log.readline()).split(":")[1].split("\\n")[0])
    print ("Informacion encontrada: " + str(flag) + "\t" + str(count))
    log.close()
except IndexError:
    flag = 0
    count = 1

key = False
key2 = False
archivo = open("Hoteles.txt", "a")
calificacion = open("Calificacion.txt", "a")
log = open("log.log", "w")
i = flag
for i in trange(len(Estados)):
    try:
        try:
            query_result = google_places.nearby_search(location=Estados[i], keyword='Hotel', radius=20000)
        except:

            # Validación para que el codigo no deje de ejecutarse en caso de superar el numero de consultas
            if key == False:
                print "\n\n Cambiando API_KEY"
                YOUR_API_KEY = 'AIzaSyDloyuFzy4k_wJAsvKTeEgktMjWYiRoTGc'
                google_places = GooglePlaces(YOUR_API_KEY)
                try:
                    query_result = google_places.nearby_search(location=Estados[i], keyword='Hotel', radius=20000)
                except:
                    print "\n\n Cambiando API_KEY (Otra vez)"
                    YOUR_API_KEY = 'AIzaSyBjUmU3tjg4t7iLH9pZN27T_I4QE0mfdms'
                    google_places = GooglePlaces(YOUR_API_KEY)
                    query_result = google_places.nearby_search(location=Estados[i], keyword='Hotel', radius=20000)
                    key2 = True
                key = True
            elif key2 == False:
                print "\n\n Cambiando API_KEY (Otra vez)"
                YOUR_API_KEY = 'AIzaSyBjUmU3tjg4t7iLH9pZN27T_I4QE0mfdms'
                google_places = GooglePlaces(YOUR_API_KEY)
                query_result = google_places.nearby_search(location=Estados[i], keyword='Hotel', radius=20000)
                key2 = True
            else:
                print "Espera 24hrs..."
                log.write("Estado:" + str(i - 1) + "\nHotelid:" + str(count))
                break

        if query_result.has_attributions:
            print query_result.html_attributions

        # Recuperar los lugares que regreso la consulta
        for place in query_result.places:

            urlfotos = ""
            try:
                place.get_details()
                try:
                    for photos in place.photos:
                        photos.get(maxheight=500, maxwidth=500)
                        urlfotos += photos.url.encode('utf-8') + ","
                except:
                    urlfotos = " "

                # Almacena la información del hotel
                archivo.write(
                    "(" + str(count) + ",\'" + place.name.encode('utf-8') + "\' , \'" + place.formatted_address.encode(
                        'utf-8') + "\' , \'Hotel Agregado por Google \' ," + str(
                        i + 1) + ", \'" + place.international_phone_number.encode(
                        'utf-8') + "\' , \'" + place.website.encode('utf-8') + "\', \"" + urlfotos + "\"),\n")

                try:
                    # Almacena la calificación promedio otorgada por los «Local Guides» de Google del lugar recuperado y almacenada como un entero para el usuario Google.
                    calificacion.write("(" + str(count) + ", \'" + str(place.rating) + "\' ," + str(count) + ", 2), \n")
                except:
                    calificacion.write("(" + str(count) + ", \' 0 \' ," + str(count) + ", 2), \n")

                count += 1
            except AttributeError:
                pass
    except:
        pass

archivo.close()
calificacion.close()
log.close()
