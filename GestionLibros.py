class Libro:
    def __init__(self, isbn: str, titulo: str, autor: str, stock: int):
        self.set_isbn(isbn)
        self.__titulo = titulo
        self.autor = autor
        self.stock = stock

    def set_isbn(self, isbn: str):
        if isbn.isdigit() and len(isbn) == 5:
            self.__isbn = isbn
        else:
            self.__isbn = "00000"

    def get_isbn(self):
        return self.__isbn

    def get_titulo(self):
        return self.__titulo

    def prestar(self):
        if self.stock > 0:
            self.stock -= 1
            return True
        return False

    def devolver(self):
        self.stock += 1


class Biblioteca:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.catalogo = []

    def get_libro(self, isbn: str):
        for libro in self.catalogo:
            try:
                if libro.get_isbn() == isbn:
                    return libro
            except AttributeError:
                continue
        return None

    def agregar_libro(self):
        print("\n--- Agregar Libro ---")
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor: ")
        isbn = input("Ingrese el ISBN (exactamente 5 dígitos numéricos): ")
        
        libro_existente = self.get_libro(isbn)
        if libro_existente:
            extra_stock = int(input(f"El libro ya existe. ¿Cuántas unidades de stock desea agregar?: "))
            libro_existente.stock += extra_stock
            print("¡Stock actualizado correctamente!")
        else:
            stock = int(input("Ingrese la cantidad de stock inicial: "))
            nuevo_libro = Libro(isbn, titulo, autor, stock)
            self.catalogo.append(nuevo_libro)
            print("¡Libro agregado al catálogo correctamente!")

    def prestar_libro(self):
        print("\n--- Prestar Libro ---")
        isbn = input("Ingrese el ISBN del libro a prestar: ")
        libro = self.get_libro(isbn)
        
        if libro is None:
            print("Error: No se encontró ningún libro con ese ISBN.")
            return

        if libro.prestar():
            print(f"¡Préstamo exitoso! Se prestó el libro '{libro.get_titulo()}'. Stock restante: {libro.stock}")
        else:
            print(f"Lo sentimos, el libro '{libro.get_titulo()}' no tiene stock disponible.")

    def devolver_libro(self):
        print("\n--- Devolver Libro ---")
        isbn = input("Ingrese el ISBN del libro a devolver: ")
        libro = self.get_libro(isbn)
        
        if libro is None:
            print("Error: El libro no pertenece a esta biblioteca.")
            return

        libro.devolver()
        print(f"¡Devolución exitosa! El libro '{libro.get_titulo()}' recuperó stock. Stock actual: {libro.stock}")

    def consultar_catalogo(self):
        if not self.catalogo:
            print("\nNo hay libros registrados en la biblioteca.")
            return
        print(f"\n=== Catálogo de la {self.nombre} ===")
        for libro in self.catalogo:
            try:
                isbn = libro.get_isbn()
            except AttributeError:
                isbn = "Desconocido"
            print(f"ISBN: {isbn} \nTítulo: {libro.get_titulo()} \nAutor: {libro.autor} \nStock: {libro.stock}\n")


def menu():
    print("\n==================================")
    print("   SISTEMA DE GESTIÓN DE LIBROS")
    print("==================================")
    print("1- Agregar / Reponer Libro")
    print("2- Prestar Libro")
    print("3- Devolver Libro")
    print("4- Consultar Estado del Catálogo")
    print("5- Salir")
    return input("Seleccione una opción: ")


def main():
    biblioteca = Biblioteca("Biblioteca Central")
    while True:
        opcion = menu()
        if opcion == "5":
            print("Programa Terminado")
            break
        elif opcion == "1":
            biblioteca.agregar_libro()
        elif opcion == "2":
            biblioteca.prestar_libro()
        elif opcion == "3":
            biblioteca.devolver_libro()
        elif opcion == "4":
            biblioteca.consultar_catalogo()
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()