"""
Si se programa como tarea, se ejecutara solo y nos dira lo que hay
"""

#urllib para la parte del web scrapping, msvcrt para dejar la ventana abierta, winsound para emitir un beep, os para hacer taskkill al cmd, time para la informacion de fecha y hora
import urllib.request, msvcrt, winsound, os, time

#funcion para descargarnos el magnet del capitulo si esta disponible,recibe como parametro, la palabra clave de la serie
def descargarMagnet(busqueda):
	#palabra a buscar, la clave de la serie que pasamos como parametro
	buscar=busqueda
	#primera ocurrencia de la palabra, buscada en el HTML, el -15 es una convencion de la web en concreto, recoge el primer valor del enlace al capitulo concreto
	start_index=str(data[0:14500]).find(buscar)-15
	#+20 para llegar al final del enlace del capitulo concreto
	last_index=start_index+len(buscar)+20
	#crea el preenlace, sin el http://...., cortando la pagina por el primer y ultimo index
	preenlace=str(data[start_index:last_index])
	#aqui juntamos el enlace completo con el del capitulo concreto (http://www.elitetorrent.net/torrent...)
	enlace=url+preenlace
	#volvemos a la parte del webscrapping para entrar al nuevo enlace y sacar el HTML
	requestEnlace=urllib.request.Request(enlace,None,headers)
	responseEnlace=urllib.request.urlopen(requestEnlace)
	dataEnlace=responseEnlace.read().decode('utf-8')
	#palabras a buscar para encontrar el link magnet (cosas de la web)
	buscar='"magnet'
	buscar2='" class="enlace_torrent degradado1">Descargar por magnet'
	#identico que antes, primer y ultimo index del enlace magnet
	start_magnet=str(dataEnlace).find(buscar)+1
	last_magnet=str(dataEnlace).find(buscar2)
	#recogemos de la pagina el enlace magnet, cuyo primer y ultimo caracteres son los index
	magnet=str(dataEnlace[start_magnet:last_magnet])
	#al ser un archivo, no un enlace propiamente dicho, necesitamos que lo abra el Sistema Operativo, asi abrimos el archivo... ET VOILA!
	os.startfile(magnet)

#Parte del Web Scrapping
#definimos el user_agent para que la pagina nos detecte como un navegador y no como un script de python, puede ser cualquier user_agent
user_agent='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
#url a la que vamos a acceder
url="http://www.elitetorrent.net"
#diccionario que contiene el user_agent con la clave User-Agent (necesaria para despues)
headers={'User-Agent':user_agent,}
#definimos la request (pagina a la que vamos, data=none(http Post no queremos), el header que tiene que ser pasado como diccionario)
request=urllib.request.Request(url,None,headers)
#abrimos la request, que viene siendo la url pero con los headers implementados, si no hicieran falta los headers, se podria pasar direcamente la url al .urlopen
response=urllib.request.urlopen(request)
#recogemos en la variable la respuesta leida que viene a ser el html de la pagina, en tipo Byte por lo que habra que castearlo a str despues y en UTF-8 (IMPORTANTISIMO)
data=response.read().decode('utf-8')

#Imprime el dia y la hora
print(time.strftime("%d/%m/%y")+" "+time.strftime("%H:%M:%S"))

#Parte de busqueda, busca la palabra clave en el trozo de codigo correspondiente a las 2 primeras columnas de la pagina aproximadamente, imprime por pantalla que lo encontro y sube el contador de capitulos a 1 para que no salte el ultimo if
contadorCapitulo=0
if str(data[0:14500]).find("theory")!=-1:
	print("Nuevo capitulo de 'The Big Bang Theory'")
	descargarMagnet("theory")
	contadorCapitulo+=1
if str(data[0:14500]).find("mentes-criminales")!=-1:
	print("Nuevo capitulo de 'Mentes Criminales'")
	descargarMagnet("mentes-criminales")
	contadorCapitulo+=1
if str(data[0:14500]).find("puro-genio")!=-1:
	print("Nuevo capitulo de 'Puro Genio'")
	descargarMagnet("puro-genio")
	contadorCapitulo+=1
if str(data[0:14500]).find("elementary")!=-1:
	print("Nuevo capitulo de 'Elementary'")
	descargarMagnet("elementary")
	contadorCapitulo+=1
if str(data[0:14500]).find("codigo-negro")!=-1:
	print("Nuevo capitulo de 'Codigo Negro'")
	descargarMagnet("codigo-negro")
	contadorCapitulo+=1
if str(data[0:14500]).find("bones")!=-1:
	print("Nuevo capitulo de 'Bones'")
	descargarMagnet("bones")
	contadorCapitulo+=1
if str(data[0:14500]).find("legion")!=-1:
	print("Nuevo capitulo de 'Legion'")
	descargarMagnet("legion")
	contadorCapitulo+=1
if str(data[0:14500]).find("the-man-in-the-high-castle")!=-1:
	print("Nuevo capitulo de 'The Man in the High Castle'")
	descargarMagnet("the-man-in-the-high-castle")
	contadorCapitulo+=1
if str(data[0:14500]).find("goliath")!=-1:
	print("Nuevo capitulo de 'Goliath'")
	descargarMagnet("goliath")
	contadorCapitulo+=1
if str(data[0:14500]).find("ransom")!=-1:
	print("Nuevo capitulo de 'Ransom'")
	descargarMagnet("ransom")
	contadorCapitulo+=1
if str(data[0:14500]).find("lies")!=-1:
	print("Nuevo capitulo de 'Big Little Lies'")
	descargarMagnet("big-little-lies")
	contadorCapitulo+=1
if str(data[0:14500]).find("como-defender-a-un-asesino")!=-1:
	print("Nuevo capitulo de 'Como Defender a un Asesino'")
	descargarMagnet("como-defender-a-un-asesino")
	contadorCapitulo+=1

#Si no encontro ningun capitulo, el contador nunca sube por lo tanto sigue en 0, pita y se cierra la ventana
if contadorCapitulo==0:
	print("Nada nuevo!")
	winsound.Beep(700,500) #Pitido para determinar que no encontro nada, 700 es la frecuencia del sonido(700=agudo) y 500 es el tiempo en ms(500=medio segundo)
	os.system('taskkill /F /IM cmd.exe') #System de la libreria OS, ejecuta el comando de windows en este caso que le pases como parametro, en este caso cerrando la ventana del cmd

#Para que no se cierre la ventana de la consola si encuentra algun capitulo
if contadorCapitulo>0:
	msvcrt.getch() #Queda a la espera de que pulsemos una tecla
