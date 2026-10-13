class Estudiante:
    def __init__(self, matricula: str, nombre: str, apellido: str, carrera: str):
        self.set_matricula(matricula)
        self.__nombre = nombre
        self.apellido = apellido
        self.carrera = carrera
        self.cursos_inscritos = []

    def set_matricula(self, matricula: str):
        if matricula.isdigit() and len(matricula) < 6:
            self.__matricula = matricula
        else:
            self.__matricula = "00000"

    def get_matricula(self):
        return self.__matricula

    def get_nombre(self):
        return self.__nombre

    def inscribir_curso(self, curso):
        self.cursos_inscritos.append(curso)

    def dar_de_baja_curso(self, curso):
        if curso in self.cursos_inscritos:
            self.cursos_inscritos.remove(curso)


class Curso:
    def __init__(self, nombre_curso: str, codigo: str, profesor: str, capacidad: int):
        self.nombre_curso = nombre_curso
        self.codigo = codigo
        self.profesor = profesor
        self.capacidad = capacidad
        self.estudiantes_inscritos = []

    def esta_disponible(self):
        return len(self.estudiantes_inscritos) < self.capacidad

    def inscribir_estudiante(self, estudiante):
        if self.esta_disponible():
            self.estudiantes_inscritos.append(estudiante)

    def dar_de_baja_estudiante(self, estudiante):
        if estudiante in self.estudiantes_inscritos:
            self.estudiantes_inscritos.remove(estudiante)


class Facultad:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.estudiantes = []
        self.cursos = []

    def get_estudiante(self, matricula: str):
        for est in self.estudiantes:
            try:
                if est.get_matricula() == matricula:
                    return est
            except AttributeError:
                continue
        return None

    def get_curso(self, codigo: str):
        for curso in self.cursos:
            if curso.codigo == codigo:
                return curso
        return None

    def agregar_estudiante(self):
        print("\n--- Registrar Estudiante ---")
        nombre = input("Ingrese el nombre del estudiante: ")
        apellido = input("Ingrese el apellido del estudiante: ")
        matricula = input("Ingrese la matrícula (hasta 5 dígitos numéricos): ")
        carrera = input("Ingrese la carrera: ")
        
        estudiante_obj = Estudiante(matricula, nombre, apellido, carrera)
        self.estudiantes.append(estudiante_obj)
        print("¡Estudiante registrado correctamente!")

    def agregar_curso(self):
        print("\n--- Registrar / Gestionar Curso ---")
        nombre_curso = input("Ingrese el nombre del curso: ")
        codigo = input("Ingrese el código del curso: ")
        profesor = input("Ingrese el nombre del profesor a cargo: ")
        
        curso_existente = self.get_curso(codigo)
        if curso_existente:
            capacidad_extra = int(input(f"El curso '{curso_existente.nombre_curso}' ya existe. ¿Cuántas vacantes desea agregar?: "))
            curso_existente.capacidad += capacidad_extra
            print("¡Capacidad del curso actualizada correctamente!")
        else:
            capacidad = int(input("Ingrese la capacidad máxima del curso: "))
            curso_obj = Curso(nombre_curso, codigo, profesor, capacidad)
            self.cursos.append(curso_obj)
            print("¡Curso agregado correctamente!")

    def inscribir_estudiante_en_curso(self):
        print("\n--- Inscribir Estudiante a Curso ---")
        matricula = input("Ingrese la matrícula del estudiante: ")
        codigo = input("Ingrese el código del curso: ")
        
        estudiante = self.get_estudiante(matricula)
        if estudiante is None:
            print("Error: El estudiante no existe o la matrícula no es válida.")
            return

        curso = self.get_curso(codigo)
        if curso is None:
            print("Error: El curso no existe.")
            return

        if curso.esta_disponible():
            curso.inscribir_estudiante(estudiante)
            estudiante.inscribir_curso(curso)
            print(f"¡Inscripción de '{estudiante.get_nombre()}' en '{curso.nombre_curso}' realizada con éxito!")
        else:
            print("Lo sentimos, no hay cupos disponibles en este curso.")

    def dar_de_baja_estudiante_de_curso(self):
        print("\n--- Dar de Baja Estudiante de Curso ---")
        matricula = input("Ingrese la matrícula del estudiante: ")
        codigo = input("Ingrese el código del curso: ")
        
        estudiante = self.get_estudiante(matricula)
        curso = self.get_curso(codigo)
        
        if estudiante is None or curso is None:
            print("Error: Datos incorrectos. Verifique la matrícula y el código del curso.")
            return

        curso.dar_de_baja_estudiante(estudiante)
        estudiante.dar_de_baja_curso(curso)
        print("El estudiante ha sido dado de baja del curso correctamente.")

    def consultar_estado_cursos(self):
        if not self.cursos:
            print("\nNo hay cursos registrados en la facultad.")
            return
        print(f"\n=== Estado de Cursos - {self.nombre} ===")
        for curso in self.cursos:
            inscritos = len(curso.estudiantes_inscritos)
            disponibles = curso.capacidad - inscritos
            print(f"Código: {curso.codigo} \nCurso: {curso.nombre_curso} \nProfesor: {curso.profesor} \nInscritos: {inscritos} \nCupos disponibles: {disponibles}\n")

    def consultar_estado_estudiantes(self):
        if not self.estudiantes:
            print("\nNo hay estudiantes registrados en la facultad.")
            return
        print(f"\n=== Estado de Estudiantes - {self.nombre} ===")
        for est in self.estudiantes:
            try:
                matricula = est.get_matricula()
            except AttributeError:
                matricula = "No registrada"
            print(f"Nombre: {est.get_nombre()} {est.apellido} \nMatrícula: {matricula} \nCarrera: {est.carrera}")
            print("Cursos inscritos:")
            if not est.cursos_inscritos:
                print("   - Ningún curso inscrito.")
            else:
                for curso in est.cursos_inscritos:
                    print(f"   - {curso.nombre_curso} (Código: {curso.codigo})")
            print("-" * 30)


def menu():
    print("\n==================================")
    print("   SISTEMA DE GESTIÓN DE FACULTAD")
    print("==================================")
    print("1- Registrar Estudiante")
    print("2- Registrar / Ampliar Curso")
    print("3- Inscribir Estudiante a Curso")
    print("4- Dar de baja Estudiante de Curso")
    print("5- Consultar Estado de Cursos")
    print("6- Consultar Estado de Estudiantes")
    print("7- Salir")
    return input("Seleccione una opción: ")


def main():
    facultad = Facultad("Facultad de Ingeniería")
    while True:
        opcion = menu()
        if opcion == "7":
            print("Programa Terminado")
            break
        elif opcion == "1":
            facultad.agregar_estudiante()
        elif opcion == "2":
            facultad.agregar_curso()
        elif opcion == "3":
            facultad.inscribir_estudiante_en_curso()
        elif opcion == "4":
            facultad.dar_de_baja_estudiante_de_curso()
        elif opcion == "5":
            facultad.consultar_estado_cursos()
        elif opcion == "6":
            facultad.consultar_estado_estudiantes()
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()