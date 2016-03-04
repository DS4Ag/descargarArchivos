# Obtener los nombres de los archio de un directorio
import os

fh = open('c:\\Users\\LVARGAS\\Documents\\MEGA\\Bases_de_datos\\2016 Consultas\\Administracion\\names.txt')
newNameFile = list()
for line in fh:
	line = line.strip()
	newNameFile.append(line)
fh.close()
print '\n ###### Los nombres se han guardado en la lista \n'
print 'La longitud de la lista de nombres es: ', len(newNameFile),'\n'

dirname = 'c:\\Users\\LVARGAS\\Documents\\MEGA\\Bases_de_datos\\2016 Consultas\\Administracion\\Bitacoras Oficiales\\ae'
directorio = os.listdir(dirname)

conteo = 0
for archivo in directorio:
	fname = raw_input("Enter para renombrar archivo (done para salir):")
	if fname == "done":
		break
	nombre = newNameFile[conteo]+'.pdf'
	print archivo, " nuevo ", nombre
	file = 'c:\\Users\\LVARGAS\\Documents\\MEGA\\Bases_de_datos\\2016 Consultas\\Administracion\\Bitacoras Oficiales\\ae\\'+archivo
	nuevoNombre = os.rename(file,nombre)
	print "Nombre anterior: ", archivo, " Nuevo nombre", nuevoNombre
	conteo = conteo + 1
print '\n ############## Se han echo todos los cambios \n'
