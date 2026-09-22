###Ejercicio 1: Sistema de Gestión de LIBROS###

from excepciones import LibroNoEncontradoError, SinStockError

class Libro:
    def __init__(self, isbn: str, titulo: str, autor: str, stock: int):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.stock = stock

    def prestar(self):
        if self.stock <= 0:
            raise SinStockError(f"No hay stock disponible para '{self.titulo}'.")
        self.stock -= 1

    def devolver(self):
        self.stock += 1

    def __str__(self):
        return f"[{self.isbn}] {self.titulo} - {self.autor} (Stock: {self.stock})"


class Biblioteca:
    def __init__(self):
        self.catalogo = {}

    def agregar_libro(self, libro: Libro):
        self.catalogo[libro.isbn] = libro

    def buscar_libro(self, isbn: str) -> Libro:
        if isbn not in self.catalogo:
            raise LibroNoEncontradoError(f"No se encontró el libro con ISBN {isbn}.")
        return self.catalogo[isbn]

    def prestar_libro(self, isbn: str):
        libro = self.buscar_libro(isbn)
        libro.prestar()

    def devolver_libro(self, isbn: str):
        libro = self.buscar_libro(isbn)
        libro.devolver()

#Plan de pruebas:  
| ID | Módulo / Clase | Escenario / Acción de Prueba | Excepción Esperada | Resultado Esperado / Mensaje Lanzado | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CP-01** | `Biblioteca` / `GestorLibros` | Buscar o devolver un libro pasando un ISBN que no existe en el sistema. | `LibroNoEncontradoError` | Notifica que el libro no existe. | Aprobado |
| **CP-02** | `Libro` | Intentar prestar un libro cuya cantidad/stock disponible es `0`. | `SinStockError` | Interrumpe el préstamo notificando que no quedan ejemplares. | Aprobado |
| **CP-03** | `Facultad` | Buscar o inscribir en una materia con un código inexistente (ej. `"MAT999"`). | `MateriaNoEncontradaError` | Lanza: `"La materia con código 'MAT999' no existe."` | Aprobado |
| **CP-04** | `Materia` | Intentar inscribir a un estudiante en una materia que alcanzó su `cupo_maximo`. | `CupoLlenoError` | Lanza: `"No hay cupo disponible en la materia [Nombre] (Máximo: [Cupo])."` | Aprobado |
| **CP-05** | `Materia` | Inscribir a un estudiante cuyo legajo ya figura en `estudiantes_inscriptos`. | `EstudianteYaInscriptoError` | Lanza: `"El estudiante [Nombre] ya está inscripto en [NombreMateria]."` | Aprobado |

##Ejercicio 2: Sistema de Gestión de FACULTAD##

from excepciones import MateriaNoEncontradaError, CupoLlenoError, EstudianteYaInscriptoError

class Estudiante:
    def __init__(self, legajo: str, nombre: str):
        self.legajo = legajo
        self.nombre = nombre

    def __str__(self):
        return f"[{self.legajo}] {self.nombre}"


class Materia:
    def __init__(self, codigo: str, nombre: str, cupo_maximo: int):
        self.codigo = codigo
        self.nombre = nombre
        self.cupo_maximo = cupo_maximo
        self.estudiantes_inscriptos = {}  # {legajo: Estudiante}

    def inscribir_estudiante(self, estudiante: Estudiante):
        if estudiante.legajo in self.estudiantes_inscriptos:
            raise EstudianteYaInscriptoError(
                f"El estudiante {estudiante.nombre} ya está inscripto en {self.nombre}."
            )
        if len(self.estudiantes_inscriptos) >= self.cupo_maximo:
            raise CupoLlenoError(
                f"No hay cupo disponible en la materia {self.nombre} (Máximo: {self.cupo_maximo})."
            )
        self.estudiantes_inscriptos[estudiante.legajo] = estudiante


class Facultad:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.materias = {}  # {codigo_materia: Materia}

    def agregar_materia(self, materia: Materia):
        self.materias[materia.codigo] = materia

    def buscar_materia(self, codigo: str) -> Materia:
        if codigo not in self.materias:
            raise MateriaNoEncontradaError(f"La materia con código '{codigo}' no existe.")
        return self.materias[codigo]

    def inscribir_alumno_en_materia(self, codigo_materia: str, estudiante: Estudiante):
        materia = self.buscar_materia(codigo_materia)
        materia.inscribir_estudiante(estudiante)

### Plan de Pruebas: Ejercicio 2 (Facultad)
| ID | Módulo / Clase | Escenario / Acción de Prueba | Excepción Esperada | Resultado Esperado / Mensaje Lanzado | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- |
