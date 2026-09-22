# Plan de Pruebas: 

| ID | Módulo / Clase | Escenario / Acción de Prueba | Excepción Esperada | Resultado Esperado / Mensaje Lanzado | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CP-01** | `Biblioteca` / `GestorLibros` | Buscar o devolver un libro pasando un ISBN que no existe en el sistema. | `LibroNoEncontradoError` | Notifica que el libro no existe. | Aprobado |
| **CP-02** | `Libro` | Intentar prestar un libro cuya cantidad/stock disponible es `0`. | `SinStockError` | Interrumpe el préstamo notificando que no quedan ejemplares. | Aprobado |
| **CP-03** | `Facultad` | Buscar o inscribir en una materia con un código inexistente (ej. `"MAT999"`). | `MateriaNoEncontradaError` | Lanza: `"La materia con código 'MAT999' no existe."` | Aprobado |
| **CP-04** | `Materia` | Intentar inscribir a un estudiante en una materia que alcanzó su `cupo_maximo`. | `CupoLlenoError` | Lanza: `"No hay cupo disponible en la materia [Nombre] (Máximo: [Cupo])."` | Aprobado |
| **CP-05** | `Materia` | Inscribir a un estudiante cuyo legajo ya figura en `estudiantes_inscriptos`. | `EstudianteYaInscriptoError` | Lanza: `"El estudiante [Nombre] ya está inscripto en [NombreMateria]."` | Aprobado |

### Ejercicio 2 (Facultad)

| ID | Módulo / Clase | Escenario / Acción de Prueba | Excepción Esperada | Resultado Esperado / Mensaje Lanzado | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CP-01** | `Materia` | Intentar inscribir a un estudiante cuyo legajo ya existe en `estudiantes_inscriptos`. | `EstudianteYaInscriptoError` | Lanza: `"El estudiante {estudiante.nombre} ya está inscripto en {self.nombre}."` | Aprobado |
| **CP-02** | `Materia` | Intentar inscribir a un estudiante cuando la cantidad de inscriptos es mayor o igual a `cupo_maximo`. | `CupoLlenoError` | Lanza: `"No hay cupo disponible en la materia {self.nombre} (Máximo: {self.cupo_maximo})."` | Aprobado |
| **CP-03** | `Facultad` | Buscar una materia con un código que no está registrado en el diccionario `materias`. | `MateriaNoEncontradaError` | Lanza: `"La materia con código '{codigo}' no existe."` | Aprobado |
| **CP-04** | `Facultad` | Inscribir un alumno llamando a `inscribir_alumno_en_materia` pasando un código de materia inexistente. | `MateriaNoEncontradaError` | La función llama a `buscar_materia` e interrumpe la inscripción lanzando la excepción. | Aprobado |
