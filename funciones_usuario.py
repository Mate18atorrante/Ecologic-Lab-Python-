#hola shinos hermosoos

#this is para el menu

#función para que el usuario ingrese sus datos
def ingreso_usu_datos():
    nom = input("Ingrese su nombre: ")
    tools = {}
    i = 0
    print(f"Muy bien {nom}, ahora ingrese los aparatos electrónicos que tiene en su hogar.")
    while True:
        tools[i] = input(f"Ingrese el aparato Nro {i+1}: ")
        eleccion = int(input("¿Desea finalizar (0) o continuar (cualquier otro número)? :"))
        if eleccion == 0:
            break
        else:
            i += 1
    return nom, tools

nombre, aparatos = ingreso_usu_datos()

#función para escribir los datos ingresados por el usuario en un archivo .txt
def esc_usu_arch():
    with open("datos_usuario.txt","w",encoding = "utf-8") as archivo:
        archivo.write(f"Nombre del usuario: {nombre}\n")
        archivo.write("Aparatos: \n")
        for indice, aparato in aparatos.items():
            archivo.write(f"{indice+1}. {aparato}\n")






