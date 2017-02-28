"""
Si se programa como tarea, se ejecutara solo y nos dira lo que hay
"""

#urllib para la parte del web scrapping, msvcrt para dejar la ventana abierta, winsound para emitir un beep, os para hacer taskkill al cmd
import urllib.request, msvcrt, winsound, os

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
#recogemos en la variable la respuesta leida que viene a ser el html de la pagina, en tipo Byte por lo que habra que castearlo a str despues
data=response.read()

#Parte de busqueda, busca la palabra clave en el trozo de codigo correspondiente a las 2 primeras columnas de la pagina aproximadamente, imprime por pantalla que lo encontro y sube el contador de capitulos a 1 para que no salte el ultimo if
contadorCapitulo=0
if str(data[0:14500]).find("theory")!=-1:
	print("Nuevo capitulo de 'The Big Bang Theory'")
	contadorCapitulo+=1
if str(data[0:14500]).find("criminales")!=-1:
	print("Nuevo capitulo de 'Mentes Criminales'")
	contadorCapitulo+=1
if str(data[0:14500]).find("genio")!=-1:
	print("Nuevo capitulo de 'Puro Genio'")
	contadorCapitulo+=1
if str(data[0:14500]).find("elementary")!=-1:
	print("Nuevo capitulo de 'Elementary'")
	contadorCapitulo+=1
if str(data[0:14500]).find("negro")!=-1:
	print("Nuevo capitulo de 'Codigo Negro'")
	contadorCapitulo+=1
if str(data[0:14500]).find("bones")!=-1:
	print("Nuevo capitulo de 'Bones'")
	contadorCapitulo+=1
if str(data[0:14500]).find("legion")!=-1:
	print("Nuevo capitulo de 'Legion'")
	contadorCapitulo+=1
if str(data[0:14500]).find("castle")!=-1:
	print("Nuevo capitulo de 'The Man in the High Castle'")
	contadorCapitulo+=1
if str(data[0:14500]).find("goliath")!=-1:
	print("Nuevo capitulo de 'Goliath'")
	contadorCapitulo+=1
if str(data[0:14500]).find("ransom")!=-1:
	print("Nuevo capitulo de 'Ransom'")
	contadorCapitulo+=1
if str(data[0:14500]).find("lies")!=-1:
	print("Nuevo capitulo de 'Big Little Lies'")
	contadorCapitulo+=1
if str(data[0:14500]).find("asesino")!=-1:
	print("Nuevo capitulo de 'Como Defender a un Asesino'")
	contadorCapitulo+=1
"""
if str(data[0:14500]).find("100")!=-1:
	print("Nuevo capitulo de 'Los 100'")   Hasta ponerme al dia
if str(data[0:14500]).find("vikings")!=-1:
	print("Nuevo capitulo de 'Vikings'")   Hasta ponerme al dia
"""

#Si no encontro ningun capitulo, el contador nunca sube por lo tanto sigue en 0, pita y se cierra la ventana
if contadorCapitulo==0:
	print("Nada nuevo!")
	winsound.Beep(700,500) #Pitido para determinar que no encontro nada, 700 es la frecuencia del sonido(700=agudo) y 500 es el tiempo en ms(500=medio segundo)
	os.system('taskkill /F /IM cmd.exe') #System de la libreria OS, ejecuta el comando de windows en este caso que le pases como parametro, en este caso cerrando la ventana del cmd

#Para que no se cierre la ventana de la consola si encuentra algun capitulo
if contadorCapitulo>0:
	msvcrt.getch() #Queda a la espera de que pulsemos una tecla
