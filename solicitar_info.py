#En este programa vamos a solicitar datos de la persona, los cuales serán exportados a un archivo de texto.

nombre = input("Por favor, escribe tu nombre:\n")
apellidos = input("Ingresa tu apellido:\n")
genero = input("Escribe tu género M (masculino) o F (femenino):\n").upper()
fecha_nacimiento = int(input("Fecha de nacimiento (dd/mm/aaaa):\n"))
telefono = int(input("Número de teléfono:\n"))

def mostrar_datos(*informacion):
    return f"Nombre completo: {nombre} {apellidos}\nGénero: {genero}\nFecha de nacimiento: {fecha_nacimiento}\nNúmero de teléfono: {telefono}"

info_completa = mostrar_datos(nombre, apellidos, genero, fecha_nacimiento, telefono)

print(info_completa)