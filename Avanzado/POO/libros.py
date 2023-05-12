
class Libro:
    def __init__(self, titulo, autor, num_hojas):
        self.titulo = titulo
        self.autor = autor
        self.num_hojas = num_hojas
        self.tipo = "libro"


class Revista(Libro):
    def __init__(self, titulo, autor, num_hojas, editorial, color, sello):
        super().__init__(titulo, autor, num_hojas)
        self.editorial = editorial
        self.color = color
        self.sello = sello


revista = Revista("Alturas", "Merico Merini", 133,"Editorial XYZ", "Rojo", "Sello A")
