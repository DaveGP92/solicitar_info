#En este programa vamos a solicitar datos de la persona, los cuales serán exportados a un archivo de texto.
import unicodedata
datos_completos = {}

def agregar_datos(variable, dato):
    datos_completos[f"{variable}"] = dato
    return datos_completos

nombre = input("Por favor, escribe tu nombre:\n").capitalize()
agregar_datos("Nombre", nombre)
print(datos_completos)

apellidos = input("Ingresa tu apellido(s):\n").capitalize()
agregar_datos("Apellidos", apellidos)
print(datos_completos)

genero = input("Escribe tu género m (masculino) o f (femenino):\n").lower()
agregar_datos("Género", genero)
print(datos_completos)


while genero not in["m", "f"]:
    genero = input("Ingrese un género válido:\n")

dia_nacimiento = int(input(f"Día de nacimiento:\n"))

mes_nacimiento = int(input(f"Mes de nacimiento (número mes):\n"))

year_nacimiento = int(input(f"Año de nacimiento:\n"))


fecha_nacimiento = f"{dia_nacimiento}/{mes_nacimiento}/{year_nacimiento}"
agregar_datos("Fecha de nacimiento", fecha_nacimiento)
print(datos_completos)


telefono = int(input("Número de teléfono:\n"))
agregar_datos("Teléfono", telefono)
print(datos_completos)

dict_to_string = str(datos_completos)


archivo = open("datos.txt", "w")
archivo.write(dict_to_string)
archivo.close()

