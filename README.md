# Plan de Pruebas: Sistemas de Gestión (Libros y Facultad)

### Ejercicio 1 (Sistema de Gestión de Libros)

| ID | Módulo / Clase | Escenario / Acción de Prueba | Excepción / Comportamiento Esperado | Resultado Esperado / Mensaje Lanzado | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CP-01** | `Biblioteca` / `Libro` | Buscar o gestionar un libro pasando un ISBN que no existe en el sistema. | Ninguno (Retorna `None` / Validación) | Notifica que no se encontró ningún libro con ese ISBN. | Aprobado |
| **CP-02** | `Libro` | Intentar prestar un libro cuya cantidad/stock disponible es `0`. | Validación lógica (`stock > 0`) | Informa que no hay stock disponible y deniega el préstamo. | Aprobado |
| **CP-03** | `Libro` | Ingresar un ISBN con un formato incorrecto (menos o más de 5 dígitos). | Validación en `set_isbn` | Asigna por defecto el código de seguridad `"00000"`. | Aprobado |
| **CP-04** | `Biblioteca` | Volver a registrar un ISBN que ya existe en el catálogo. | Lógica de duplicados en `agregar_libro` | Detecta que el libro ya existe y pregunta cuántas unidades de stock sumar. | Aprobado |
| **CP-05** | `Biblioteca` | Consultar el catálogo cuando la lista está vacía. | Validación de lista vacía | Muestra el mensaje: "No hay libros registrados en la biblioteca." | Aprobado |


### Ejercicio 2 (Sistema de Gestión de Facultad)

| ID | Módulo / Clase | Escenario / Acción de Prueba | Excepción / Comportamiento Esperado | Resultado Esperado / Mensaje Lanzado | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CP-01** | `Estudiante` | Registrar un estudiante ingresando una matrícula que no sea numérica o supere los 5 dígitos. | Validación en `set_matricula` | Asigna por defecto la matrícula `"00000"`. | Aprobado |
| **CP-02** | `Curso` | Intentar inscribir a un estudiante cuando la cantidad de inscritos alcanzó su `capacidad` máxima. | Validación (`esta_disponible()`) | Rechaza la inscripción informando que no hay cupos disponibles. | Aprobado |
| **CP-03** | `Facultad` | Buscar una materia/curso con un código que no está registrado. | Retorna `None` | Informa que el curso no existe. | Aprobado |
| **CP-04** | `Facultad` | Inscribir un alumno pasando un código de curso o matrícula inexistente. | Validación de referencias nulas | Muestra mensaje de error indicando datos incorrectos. | Aprobado |
| **CP-05** | `Facultad` | Consultar el estado de los cursos y estudiantes con listas vacías. | Validación de colecciones vacías | Notifica que no hay cursos ni estudiantes registrados respectivamente. | Aprobado |