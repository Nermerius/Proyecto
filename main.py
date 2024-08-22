import json

def guardar_datos(datos):
	with open('inventario.json', 'w') as f:
		json.dump(datos, f)

def cagar_datos():
	with open('inventario.json', 'r') as f:
		return(json.load(f))

def crear(inventario):
	while True:
		datos = []
		datos.append(input("(escriba \'SALIR\' para regresar al menu)\nNombre del producto: "))
		if(datos[0]=="SALIR"):
			return(inventario)
		elif(datos[0] not in inventario.keys()):
			datos.append(input("Precio del producto: "))
			try:
				datos[1]=float(datos[1])
			except ValueError:
				print("Solo debe ingresar un numero.")
				continue
			if(datos[1]>=0.0):
				datos.append(input("Cantidad en stock del producto: "))
				try:
					datos[2]=int(datos[2])
				except ValueError:
					print("Solo debe ingresar un numero entero.")
					continue
				if(datos[2]>=0):
					inventario.setdefault(datos[0],{"precio":datos[1],"stock":datos[2]})
					guardar_datos(inventario)
					return(inventario)
				else:
					print("La cantidad de Stock que puso es negativo.")
			else:
				print("El precio que puso es negativo.")
		else:
			print("Ya esta el nombre \'"+str(datos[0])+"\' entre los productos del inventario.")

def mostrar(inventario):
	print("Nombre-----------------Precio-----------------Cantidad en stock\n")
	for nombre in sorted(inventario):
		if(len(nombre)<20):
			print(nombre,end=(23-len(nombre))*"-")
		else:
			print(nombre[:19],end="...-")
		print(inventario[nombre]["precio"],end=(""))
		if(len(str(inventario[nombre]["precio"]))<22):
			print((23-len(str(inventario[nombre]["precio"])))*"-",end=(""))
		else:
			print("-",end=(""))
		print(inventario[nombre]["stock"])

def mostrar_producto(inventario,nombre):
	if(nombre in inventario.keys()):
		print("\nNombre: "+str(nombre))
		print("Precio: "+str(inventario[nombre]["precio"]))
		print("Cantidad en stock: "+str(inventario[nombre]["stock"]))
	else:
		print("\nNo existe ningun producto con el nombre \'"+str(nombre)+"\' entre los productos guardados.")

def modificar(inventario):
	while True:
		nombre = input("(escriba \'SALIR\' para regresar al menu)\nNombre del producto que desea modificar: ")
		if(nombre=="SALIR"):
			return(inventario)
		elif(nombre in inventario.keys()):
			while True:
				opciones = input("\nProducto selecionado \'"+str(nombre)+"\'\n\n1. Si desea cambiar el nombre del producto.\n2. Si desea cambiar el precio del producto.\n3. Si desea cambiar la cantidad de stock del producto.\n4. Si desea cambiar el producto que quieres modificar.\n5. Si desea regresar al menu.\n\nElige una opción: ")
				if(str(opciones)=="1"):
					opciones=input("\n(Anterior nombre "+str(nombre)+")\nEscriba el nuevo nombre del producto: ")
					if(opciones not in inventario.keys()):
						inventario.setdefault(opciones,{"precio":inventario[nombre]["precio"],"stock":inventario[nombre]["stock"]})
						del(inventario[nombre])
						guardar_datos(inventario)
						nombre = opciones
					else:
						print("Ya esta el nombre \'"+str(opciones)+"\' entre los productos del inventario.")
				elif(str(opciones)=="2"):
					opciones=input("\n(Anterior precio "+str(inventario[nombre]["precio"])+")\nEscriba el nuevo precio del producto: ")
					try:
						inventario[nombre]["precio"]=float(opciones)
						guardar_datos(inventario)
					except ValueError:
						print("Solo debe ingresar un numero.")
						continue
				elif(str(opciones)=="3"):
					opciones=input("\n(Cantidad anterior de stock "+str(inventario[nombre]["stock"])+")\nEscriba la nueva cantidad de stock del producto: ")
					try:
						inventario[nombre]["stock"]=int(opciones)
						guardar_datos(inventario)
					except ValueError:
						print("Solo debe ingresar un numero entero.")
						continue
				elif(str(opciones)=="4"):
					break
				elif(str(opciones)=="5"):
					return(inventario)
				else:
					print("\n\'"+str(opciones)+"\' no esta entre las opciones.")
		else:
			print("No existe ningun producto con el nombre \'"+str(nombre)+"\' entre los productos guardados.")

def eliminar(inventario):
	while True:
		nombre = input("(escriba \'SALIR\' para regresar al menu)\nNombre del producto que desea eliminar: ")
		if(nombre=="SALIR"):
			return(inventario)
		elif(nombre in inventario.keys()):
			del(inventario[nombre])
			guardar_datos(inventario)
			return(inventario)
		else:
			print("No existe ningun producto con el nombre \'"+str(nombre)+"\' entre los productos guardados.")

def menu():
	inventario = cagar_datos()
	while True:
		opcion = input("--- Gestión de Inventario ---\n\n1. Crear producto\n2. Mostrar todos los productos\n3. Mostrar información de un producto\n4. Actualizar producto\n5. Eliminar producto\n6. Salir\n\nElige una opción: ")
		if(str(opcion)=="1"):
			inventario = crear(inventario)
		elif(str(opcion)=="2"):
			mostrar(inventario)
		elif(str(opcion)=="3"):
			mostrar_producto(inventario,input("Nombre del producto: "))
		elif(str(opcion)=="4"):
			inventario = modificar(inventario)
		elif(str(opcion)=="5"):
			inventario = eliminar(inventario)
		elif(str(opcion)=="6"):
			return()
		else:
			print("\n\'"+str(opcion)+"\' no esta entre las opciones.")
		print("")

menu()