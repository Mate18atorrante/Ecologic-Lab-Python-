#usamos os.system("cls" if os.name == "nt" else "clear") para limpiar la consola independientemente del sistema operativo del usuario
import os

textos = (" ------------------ MENÚ ------------------ ", " Registrar un nuevo aparato", " Registrar nueva acción sostenible", " Resumen de acciones sostenibles semanal", " Salir al Escritorio","Está seguro/a?\nSi / No","Nombre de Aparato / NO para salir: ","Horas de uso: ","Cerrando programa...","No se registraron aparatos.","|Aparatos|Horas de uso|","Ahora presione Enter para volver al MENÚ: ","Aparatos registrados", "Has registrado")
aparatos = []
horas = []

def guardar_datos():
	ruta = os.path.abspath("aparatos.txt")
	with open(ruta, "w", encoding="utf-8") as archivo:
		for i in range(len(aparatos)):
			archivo.write(f"{aparatos[i]},{horas[i]}\n")
	print(f"\n✅ Datos guardados.")

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
		print("📂 Datos cargados")
	else:
		print("ℹ️ Es un usuario nuevo.")

def confirmar_opcion(i):
	print(f"Eligió {textos[i]}. {textos[5]}")
	while True:
		x = str.lower(str(input("Respuesta: ")))
		if x in ("si", "no"):
			break
		else:
			os.system("cls" if os.name == "nt" else "clear")
			print("❗Debe ingresar SI o NO para continuar.")
	return x

def interfaz():
	os.system("cls" if os.name == "nt" else "clear")
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

	intentos = 0
	if len(aparatos) == 0:
		while True:
			try:
				opcion_menu = int(input("Seleccione una opción (1 o 2): "))
				if opcion_menu in (1,2):
					break
				else:
					print("❗ Debe ingresar 1 o 2.")
					intentos += 1
					if intentos >= 5:
						interfaz()
						return
			except ValueError:
				print("❗ Debe ingresar 1 o 2.")
				intentos += 1
				if intentos >= 5:
					interfaz()
					return
		if opcion_menu == 1: reg_aparato()
		else: salir()
	else:
		while True:
			try:
				opcion_menu = int(input("Seleccione una opción (1..4): "))
				if opcion_menu in (1,2,3,4):
					break
				else:
					print("❗ Debe ingresar un número del 1 al 4.")
					intentos += 1
					if intentos >= 5:
						interfaz()
						return
			except ValueError:
				print("❗ Debe ingresar un número del 1 al 4.")
				intentos += 1
				if intentos >= 5:
					interfaz()
					return
		if opcion_menu == 1: reg_aparato()
		elif opcion_menu == 2: reg_accion_semanal()
		elif opcion_menu == 3: resumen()
		else: salir()

def reg_aparato():
	os.system("cls" if os.name == "nt" else "clear")

	nuevos_aparatos = 0
	if confirmar_opcion(1) == "si":
		os.system("cls" if os.name == "nt" else "clear")
		decision = True
		print(f"------- {textos[1]} -------")
		while decision:
			while True:
				nuevo_aparato =  str(input(f"\n{textos[6]}")).strip().lower()

				if nuevo_aparato.isdigit():
					os.system("cls" if os.name == "nt" else "clear")
					print("❗ Debe ingresar el nombre (no números) de un aparato o NO para continuar.")
				elif nuevo_aparato.lower() in [aparato.lower() for aparato in aparatos]:
					os.system("cls" if os.name == "nt" else "clear")
					print(" 📂 Ese aparato ya está registrado.")
				else:
					break
			if nuevo_aparato != "no":
				nuevos_aparatos += 1
				aparatos.append(nuevo_aparato)
				while True:
					try:
						cant_horas = int(input(f"{textos[7]}"))
						break
					except ValueError:
						os.system("cls" if os.name == "nt" else "clear")
						print("❗ El dato introducido no es un número.")
				horas.append(cant_horas)
				print(" ✅ Nuevo Aparato registrado.")
			else:
				decision = False
		print(f" \n✅{textos[13]} {nuevos_aparatos} nuevo/s aparato/s.")
	elif nuevos_aparatos == 0:
		print(textos[9])

	input(textos[11])
	guardar_datos()
	interfaz()

def reg_accion_semanal():
	os.system("cls" if os.name == "nt" else "clear")
	if confirmar_opcion(3) == "no":
		input(textos[11])
		interfaz()
		return
	else:
		os.system("cls" if os.name == "nt" else "clear")
		print("Dispositivos registrados: ")
		for i, aparato in enumerate(aparatos):
			print(f"{i+1}. {aparato.capitalize()}")

		while True:
			seleccion = input("¿Cuál/es de ellos usaste hoy? (ingrese los números de los aparatos separados por comas): ")
			try:
				indices = [int(i.strip()) - 1 for i in seleccion.split(",") if i.strip().isdigit()]
				indices = [i for i in indices if 0 <= i < len(aparatos)]
				if not indices:
					print("No seleccionaste dispositivos válidos. Intenta nuevamente.")
					continue
				break
			except ValueError:
				print("Formato incorrecto. Usa números separados por comas (ej: 1,2,3)")

		for i in indices:
			os.system("cls" if os.name == "nt" else "clear")
			print(f"Registrando uso para: {aparatos[i].capitalize()}")
			while True:
				try:
					cant_horas = int(input(f"¿Cuántas horas usaste el aparato ({aparatos[i].capitalize()}): "))
					if cant_horas >= 0:
						break
					print("Ingresa un número positivo de horas.")
				except ValueError:
					print("Debe ingresar un número válido de horas.")
			horas[i] += cant_horas

			if cant_horas >= 8:
				print("⚠️  Son muchas horas de uso. Sería mejor que apagues ese aparato si no necesitás usarlo.")
			elif cant_horas >= 4:
				print("ℹ️  Considerá reducir el tiempo de uso si es posible.")
			elif cant_horas > 0:
				print("✅  Buen uso del dispositivo.")
			else:
				print("No registraste horas en este dispositivo.")

			if len(indices) > 1:
				input("\nPresione Enter para continuar al siguiente dispositivo->")
		guardar_datos()
		input(textos[11])
		interfaz()

def resumen():
	os.system("cls" if os.name == "nt" else "clear")
	if confirmar_opcion(3) == "si":
		os.system("cls" if os.name == "nt" else "clear")
		print(f"------- {textos[3]} -------")
		print(textos[10])

		for i in range(len(aparatos)):
			print(f"{i + 1}.|{aparatos[i].capitalize()}	|{horas[i]} hs|")
	input(textos[11])
	interfaz()

def salir():
	os.system("cls" if os.name == "nt" else "clear")
	if confirmar_opcion(4) == "si":
		print(f"\n{textos[8]}")
	else:
		input(textos[11])
		interfaz()

# ---- PROGRAMA PRINCIPAL ----
cargar_datos_guardados()
interfaz()
print("El programa finalizó.")