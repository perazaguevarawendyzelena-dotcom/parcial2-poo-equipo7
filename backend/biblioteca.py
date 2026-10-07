"""Sistema de biblioteca universitaria - Programación Orientada a Objetos."""


class MaterialBiblioteca:
    """Clase padre: atributos y comportamiento comunes a todo material."""

    def __init__(self, titulo, codigo, disponibilidad):
        self.titulo = titulo
        self.codigo = codigo
        self.disponibilidad = disponibilidad  # True = disponible, False = prestado

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponibilidad else "Prestado"
        return f"[{self.codigo}] {self.titulo} - {estado}"

    def calcular_dias_prestamo(self):
        # Cada clase hija define sus propios días de préstamo.
        raise NotImplementedError("Las clases hijas deben implementar este método")


class Libro(MaterialBiblioteca):
    def __init__(self, titulo, codigo, disponibilidad, autor):
        super().__init__(titulo, codigo, disponibilidad)
        self.autor = autor

    def mostrar_informacion(self):
        base = super().mostrar_informacion()
        return f"Libro: {base} | Autor: {self.autor}"

    def calcular_dias_prestamo(self):
        return 7


class Revista(MaterialBiblioteca):
    def __init__(self, titulo, codigo, disponibilidad, numero_edicion):
        super().__init__(titulo, codigo, disponibilidad)
        self.numero_edicion = numero_edicion

    def mostrar_informacion(self):
        base = super().mostrar_informacion()
        return f"Revista: {base} | Edición No. {self.numero_edicion}"

    def calcular_dias_prestamo(self):
        return 3


def main():
    # Libros y revistas conviven en UNA MISMA colección (lista).
    materiales = [
        Libro("Introducción a la Programación con Python", "L-001", True, "Eric Matthes"),
        Libro("Estructuras de Datos y Algoritmos", "L-002", False, "Mark Allen Weiss"),
        Revista("Ciencia y Tecnología Hoy", "R-001", True, 45),
        Revista("Innovación Universitaria", "R-002", True, 12),
    ]

    # Polimorfismo: un mismo recorrido, cada objeto ejecuta SU versión del método.
    for material in materiales:
        print(material.mostrar_informacion())
        print(f"   Días de préstamo: {material.calcular_dias_prestamo()}")


if __name__ == "__main__":
    main()
