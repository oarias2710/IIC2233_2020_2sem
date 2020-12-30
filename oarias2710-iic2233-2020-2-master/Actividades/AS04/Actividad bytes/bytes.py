import os


def reparar_imagen(ruta_entrada, ruta_salida):
    # --- COMPLETAR ---#
    with open(ruta_entrada, "rb") as archivo_bytes:
        archivo_reparado = bytearray()
        data = archivo_bytes.read(32)
        while data:
            data = data[:17]
            byte_inicial = data[0]
            data = data[1:]
            if byte_inicial == 1:
                data = data[::-1]
            archivo_reparado.extend(data)
            data = archivo_bytes.read(32)

    with open(ruta_salida, "wb") as archivo_final:
        archivo_final.write(archivo_reparado)


# --- NO MODIFICAR ---#
def reparar_imagenes(carpeta_entrada, carpeta_salida):
    for filename in os.listdir(os.path.join(os.getcwd(), carpeta_entrada)):
        reparar_imagen(
            os.path.join(os.getcwd(), carpeta_entrada, filename),
            os.path.join(os.getcwd(), carpeta_salida, filename)
        )


if __name__ == '__main__':
    try:
        # reparar_imagenes('corruptas', 'caratulas')
        reparar_imagenes('Actividad bytes/corruptas', 'Actividad bytes/caratulas')
        print("Imagenes reparadas (recuerda revisar que se carguen correctamente)")
    except Exception as error:
        print(f'Error: {error}')
        print("No has podido reparar las caratulas :'c")
