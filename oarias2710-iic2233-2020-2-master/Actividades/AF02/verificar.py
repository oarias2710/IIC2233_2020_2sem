from estudiante import cargar_datos, cargar_datos_corto


def verificar_numero_alumno(alumno):  # Levanta la excepción correspondiente
    contador = 0
    posicion = 0
    largo = len(alumno.n_alumno)
    for elem in alumno.n_alumno:
        if elem.isdigit() is False and posicion != largo - 1:
            contador += 1
        posicion += 1
    if alumno.n_alumno[0:2] != str(alumno.generacion):
        contador += 1
    if alumno.n_alumno[2:4] != str(alumno.carrera):
        contador += 1
    if contador != 0:
        raise ValueError("El número de alumno es incorrecto")


def corregir_alumno(estudiante): # Captura la excepción anterior
    try:
        verificar_numero_alumno(estudiante)
    except ValueError as error:
        print(f"Error: {error}")
        # print(estudiante.n_alumno)
        remate = estudiante.n_alumno[-1]
        cola_original = estudiante.n_alumno[4:-1]
        cola = ""
        for elem in cola_original:
            if elem.isdigit() is True:
                cola += str(elem)
            else:
                cola += "0"
        gen = str(estudiante.generacion - 2000)
        carr = ""
        if estudiante.carrera == "Ingeniería":
            carr = "63"
        elif estudiante.carrera == "College":
            carr = "61"
        n_nuevo = gen + carr + cola + remate
        # print(n_nuevo)
        estudiante.n_alumno = n_nuevo
    print(f"{estudiante.nombre} está correctamente inscrite en el curso, todo en orden... \n")


def verificar_inscripcion_alumno(n_alumno, base_de_datos): # Levanta la excepción correspondiente
    if n_alumno not in base_de_datos.keys():
        raise KeyError("El número de alumno no se encuentra en la base de datos")
    else:
        return base_de_datos[n_alumno]


def inscripcion_valida(estudiante, base_de_datos):  # Captura la excepción anterior
    try:
        verificar_inscripcion_alumno(estudiante.n_alumno, base_de_datos)
    except KeyError as error:
        print(f"Error: {error}")
        print("¡Alerta! ¡Puede ser el Dr. Pinto intentando atraparte! \n")


def verificar_nota(nota):  # Levanta la excepción correspondiente
    if type(nota) != float:
        raise TypeError("El promedio no tiene el tipo correcto")
    else:
        return True


def corregir_nota(estudiante):  # Captura la excepción anterior
    try:
        verificar_nota(estudiante.promedio)
    except TypeError as error:
        print(f"Error: {error}")
        if "," in str(estudiante.promedio):
            lista = estudiante.promedio.split(",")
            nota_nueva = float(str(lista[0]) + "." + str(lista[1]))
        else:
            nota_nueva = float(estudiante.promedio)
        estudiante.promedio = nota_nueva
    print(f"Procediendo a hacer git hack sobre {estudiante.promedio}... \n")


if __name__ == "__main__":
    datos = cargar_datos_corto("alumnos.txt")  # Se cargan los datos
    for alumno in datos.values():
        if alumno.carrera != "Profesor":
            corregir_alumno(alumno)
            inscripcion_valida(alumno, datos)
            corregir_nota(alumno)
