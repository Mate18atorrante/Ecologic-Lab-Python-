#hola shinos hermosoos

#this is para el menu

def IngresoDeDatos(nom):
    while True:
        try:
            nom = input("Ingrese su nombre: ")
        except ValueError:
            print("Debe ingresar un nombre con caracteres, no un número.")

