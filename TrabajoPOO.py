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