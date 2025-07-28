import os

textos = (" ------------------ MENÚ ------------------ ", " Registrar un nuevo aparato", " Registrar nueva acción sostenible", " Resumen de acciones sostenibles semanal", " Salir al Escritorio","Está seguro/a?\nSi / No","Nombre de Aparato / NO para salir: ","Horas de uso: ","Cerrando programa...","No se registraron aparatos.","|Aparatos|Horas de uso|","Ahora presione Enter para volver al MENÚ: ","Aparatos registrados")
aparatos = []
horas = []
intentos = 0

def confirmar_opcion(i):
	print(f"Eligió {textos[i]}. {textos[5]}")
	while True:
		try:
			x = str.lower(str(input("Respuesta: ")))
			if x in ("si", "no"):
				break
		except TypeError:
			os.system("cls")
			print("Debe ingresar SI o NO para continuar, no un número")
	return x

def cargar_datos_guardados():
	if os.path.exists("aparatos.txt"):
		with open("aparatos.txt", "r", encoding="utf-8") as archivo:
			for linea in archivo:
				partes = linea.strip().split(",")
				if len(partes) == 2:
					aparato = partes[0]
					try:
						hora = int(partes[1])
						aparatos.append(aparato)
						horas.append(hora)
					except ValueError:
						pass

def interfaz():
	os.system("cls")
	j = 0
	if len(aparatos) == 0:
		print(f"\n {textos[0]}")
		print(f"\n(1) {textos[1]}")
		print(f"\n(2) {textos[4]}")
	else:
		while j!=5:
			if j == 0:
				print(f"\n{textos[0]}")
				print(f"          {len(aparatos)} {textos[12]}")
			else:
				print(f"\n({j}){textos[j]}")
			j+=1
	selector()

def selector():
	print()
	print()

	if len(aparatos) == 0:
		while True:
			try:
				opcion_menu = int(input("Seleccione una opción (1 o 2): "))
				if opcion_menu in (1,2):
					break
			except ValueError:
				print("Debe ingresar un número (1 o 2), no caracteres.")
		if opcion_menu == 1: reg_aparato()
		else: salir()
	else:
		while True:
			try:
				opcion_menu = int(input("Seleccione una opción (1..4): "))
				if opcion_menu in (1,2,3,4):
					break
			except ValueError:
				print("Debe ingresar un número del 1 al 4, no caracteres.")
		if opcion_menu == 1: reg_aparato()
		elif opcion_menu == 2: reg_accion_semanal()
		elif opcion_menu == 3: resumen()
		else: salir()


def reg_accion_semanal():
	os.system("cls")
	if confirmar_opcion(3) == "no":
		input(textos[11])
		interfaz()
	else:
		os.system("cls")
		print("Dispositivos registrados: ")
		for i, aparato in enumerate(aparatos):
			print(f"{i+1}. {aparato.capitalize()}")

		seleccion = input("(ingrese los números de los aparatos separados por comas)\n¿Cuál/es de ellos usaste hoy?: ")
		indices = []

		try:
			indices = [int(i.strip())-1 for i in seleccion.split(",") if 0 <= int(i.strip())-1 < len(aparatos)]
		except:
			print("Entrada inválida. Volviendo al menú...")
			input(textos[11])
			interfaz()

		for i in indices:
			try:
				cant_horas = int(input(f"¿Cuántas horas usaste el aparato ({aparatos[i].capitalize()}): "))
			except:
				print("Dato no válido, se asume 0 horas.")
				cant_horas = 0
			horas[i] += cant_horas  # suma horas al uso anterior

			if cant_horas >= 8:
				print("⚠️  Son muchas horas de uso. Sería mejor que apagues ese aparato si no necesitás usarlo.")
			elif cant_horas >= 4:
				print("ℹ️  Considerá reducir el tiempo de uso si es posible.")
			elif cant_horas > 0:
				print("✅  Buen uso del dispositivo.")
			else:
				print("No registraste horas en este dispositivo.")

			input(textos[11])
			interfaz()


def salir():
	os.system("cls")
	if confirmar_opcion(4) == "si":
		print(textos[8])
	else:
		input(textos[11])
		interfaz()

def resumen():
	os.system("cls")
	if confirmar_opcion(3) == "si":
		os.system("cls")
		print(f"------- {textos[3]} -------")

		i = 0
		print(textos[10])
		while i != (len(aparatos)):
			print(f"{i+1}.|{(aparatos[i]).capitalize()}	|{(horas[i])} hs|")
			i += 1
		input(textos[11])
	interfaz()

def reg_aparato():
	os.system("cls")
	if confirmar_opcion(1) == "si":
		os.system("cls")
		decision = True
		print(f"------- {textos[1]} -------")
		while decision:
			while True:
				try:
					nuevo_aparato = str.lower(str(input(f"{textos[6]}")))
					break
				except TypeError:
					os.system("cls")
					print("Debe ingresar el nombre de un aparato o NO para continuar.")
			if nuevo_aparato != "no":
				aparatos.append(nuevo_aparato)
				while True:
					try:
						cant_horas = int(input(f"{textos[7]}"))
						break
					except TypeError:
						os.system("cls")
						print("El dato introducido no es un número.")
				horas.append(cant_horas)
			else:
				decision = False
	if len(aparatos) == 0:
		print(textos[9])
		input(textos[11])
	else:
		print(f"{len(aparatos)} {textos[12]}")
		input(textos[11])
	interfaz()

interfaz()
print("El programa finalizó.")