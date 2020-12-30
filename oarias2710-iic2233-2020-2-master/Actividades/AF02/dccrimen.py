from estudiante import cargar_datos
from verificar import corregir_alumno, corregir_nota, inscripcion_valida


class GymPro(Exception):
    # Completar
    def __init__(self, estudiante):
        super().__init__("Wait a minute... Who are you?")
        self.profesor = estudiante.nombre

    def evitar_sospechas(self):
        # Completar
        print(f"¡Cuidado, viene {self.profesor}! Solo estaba haciendo mi último push...")


if __name__ == "__main__":
    datos = cargar_datos("alumnos.txt")
    nueva_base = dict()
    for alumno in datos.values():
        corregir_alumno(alumno)
        corregir_nota(alumno)
        nueva_base[alumno.n_alumno] = alumno
    for alumno in nueva_base.values():
        try:
            # Completar
            if alumno.carrera == "Profesor":
                raise GymPro(alumno)
            else:
                alumno.promedio = float(7)
                print("Hackeando nota...")

        except GymPro as error:  # Recuerda especificar el tipo de excepción que vas a capturar
            # Completar
            print(error)
            print(error.evitar_sospechas())
