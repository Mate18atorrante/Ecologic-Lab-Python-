#usamos limpiar_consola() para limpiar la consola independientemente del sistema operativo del usuario
import os

textos = (" ~~~~~~~~~~~~~~~~~~ ¦ MENÚ ¦ ~~~~~~~~~~~~~~~~~~ ",
		  " Registrar un nuevo aparato",
		  " Eliminar un aparato",
		  " Registrar nueva acción sostenible",
		  " Resumen de acciones sostenibles semanal",
		  " Salir al Escritorio",
		  "Está seguro/a?\nSi / No",
		  "Nombre de Aparato / NO para salir: ",
		  "Horas de uso: ",
		  "No se registraron aparatos.",
		  "Ahora presione Enter para volver al ¦ MENÚ ¦: ",
		  )
aparatos = []
horas = []

def limpiar_consola():
	os.system("cls" if os.name == "nt" else "clear")
	
def guardar_datos():
	ruta = os.path.abspath("aparatos.txt")
	with open(ruta, "w", encoding="utf-8") as archivo:
		for i in range(len(aparatos)):
			archivo.write(f"{aparatos[i]},{horas[i]}\n")
	print(f"\n ✎ Datos guardados.")

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
		print("✉ Datos cargados")
	else:
		print("ℹ️ Es un usuario nuevo.")

def confirmar_opcion(i):
	print(f"Eligió {textos[i]}. {textos[6]}")
	while True:
		x = str.lower(str(input("Respuesta: ")))
		if x in ("si", "no"):
			break
		else:
			limpiar_consola()
			print("Δ Debe ingresar SI o NO para continuar.")
	return x

def interfaz():
	limpiar_consola()
	j = 0
	if len(aparatos) == 0:
		print(f"\n {textos[0]}")
		print(f"\n(1) {textos[1]}")
		print(f"\n(2) {textos[5]}")
	else:
		while j!=6:
			if j == 0:
				print(f"\n{textos[0]}")
				print(f"          {len(aparatos)} aparatos registrados")
			else:
				print(f"\n({j}){textos[j]}")
			j+=1
	selector()

def ingreso_opcion_selector(mensaje1,mensaje2):
	intentos = 0
	while True:
		try:
			opcion_menu = int(input(mensaje1))
			if (len(aparatos) == 0 and opcion_menu in (1, 2)) or (len(aparatos) > 0 and opcion_menu in (1,2,3,4,5)):
				return opcion_menu
			else:
				print(mensaje2)
				intentos += 1
				if intentos >= 5:
					interfaz()
					return
		except ValueError:
			print("Δ Solo números.")
			intentos += 1
			if intentos >= 5:
				interfaz()
				return

def selector():
	print()

	if len(aparatos) == 0:
		opcion_original = ingreso_opcion_selector("Seleccione una opción (1 o 2): ","Δ Solo los números 1 o 2.")
		if opcion_original == 1: reg_aparato()
		else: salir()
	else:
		opcion_secundaria = ingreso_opcion_selector("Seleccione una opción (1..5): ","Δ Solo números del 1 al 5.")
		if opcion_secundaria == 1: reg_aparato()
		elif opcion_secundaria == 2: eliminar_aparato()
		elif opcion_secundaria == 3: reg_accion_semanal()
		elif opcion_secundaria == 4: resumen()
		else: salir()

def reg_aparato():
	nuevos_aparatos = 0
	if confirmar_opcion(1) == "si":
		limpiar_consola()
		decision = True
		print(f"------- ¦{textos[1]}¦ -------")
		while decision:
			while True:
				nuevo_aparato =  str(input(f"\n{textos[7]}")).strip().lower()

				if nuevo_aparato.isdigit():
					print("Δ no números.")
				elif nuevo_aparato.lower() in [aparato.lower() for aparato in aparatos]:
					print(" Ξ Ese aparato ya está registrado.")
				else:
					break
			if nuevo_aparato != "no":
				nuevos_aparatos += 1
				aparatos.append(nuevo_aparato)
				while True:
					try:
						cant_horas = int(input(f"{textos[8]}"))
						break
					except ValueError:
						limpiar_consola()
						print("Δ El dato introducido no es un número.")
				horas.append(cant_horas)
				print(" + Nuevo Aparato registrado.")
			else:
				decision = False
		if nuevos_aparatos > 0:
			guardar_datos()
			print(f" \n+ Has registrado {nuevos_aparatos} nuevo/s aparato/s.")
		input(textos[10])
	interfaz()

def reg_accion_semanal():
	if confirmar_opcion(3) == "si":
		aparato_nro = 0
		limpiar_consola()
		print(f"------- ¦{textos[3]} ¦ -------")
		print("Dispositivos registrados: ")

		for i, aparato in enumerate(aparatos):
			print(f"{i+1}. {aparato.capitalize()}")
		while True:
			seleccion = input("¿Cuál/es de ellos usaste hoy? (ingrese los números de los aparatos separados por comas/ No para salir): ").strip().lower()
			if seleccion == "no":
				input(f"No se registro nada esta vez. {textos[10]}")
				interfaz()
				return
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
			aparato_nro += 1
			print("\n━━━━   ━━━━━━━━   ━━━━━━━━   ━━━━")
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

			print()
			if cant_horas >= 8:
				print("⚠  Son muchas horas de uso. Sería mejor que apagues ese aparato si no necesitás usarlo.")
			elif cant_horas >= 4:
				print("ℹ  Considerá reducir el tiempo de uso si es posible.")
			elif cant_horas > 0:
				print("★  Buen uso del dispositivo!.")
			else:
				print("No registraste horas en este dispositivo.")

			if len(indices) - aparato_nro > 0:
				input("\nPresione Enter para continuar al siguiente dispositivo->")
		guardar_datos()
		input(textos[10])
	interfaz()

def resumen():
	if confirmar_opcion(4) == "si":
		limpiar_consola()
		print(f"------- ¦{textos[4]}¦ -------")
		print("| Aparatos | Horas de uso |")

		for i in range(len(aparatos)):
			print(f"{i + 1}.| {aparatos[i].capitalize()} | {horas[i]} hs|")
		input(textos[10])
	interfaz()

def eliminar_aparato():
	if confirmar_opcion(2) == "si":
		while aparatos:
			limpiar_consola()
			print(f"------- ¦{textos[2]} ¦ -------")
			print("Dispositivos disponibles: ")
			for i, aparato in enumerate(aparatos):
				print(f"{i + 1}. {aparato.capitalize()}")

			while True:
				indice = input("Ingrese el número del aparato que desea eliminar/No para salir: ").lower().strip()
				if indice.isdigit():
					indice = int(indice) - 1
					if 0 <= indice < len(aparatos):
						decision = input(f"Eligió {indice}")
				elif indice == "no":
					input(f"No se eliminó ningún aparato esta vez. {textos[10]}")
					interfaz()
					return
				else:
					print("Solo ingrese No o el indice de un aparato.")

		else:
			print("No hay más aparatos")


		input(textos[10])
	interfaz()

def salir():
	if confirmar_opcion(5) == "si":
		print(f"\nCerrando programa...")
	else:
		interfaz()

# ---- PROGRAMA PRINCIPAL ----
cargar_datos_guardados()
interfaz()
print("El programa finalizó.")